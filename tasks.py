import celery
from celery import group
from celery.schedules import crontab
from config import dimension_configs, fact_configs, _source_conn, _output_conn
from run import load_cached_dimensions, run_dimension_etl,\
    run_fact_etl, delete_existing_dimensions_and_facts


@celery.task(time_limit=43200)
def process_etl(conf_name, conf_type):
    assert conf_type in ["dimension", "fact"]
    conf_list = dimension_configs if conf_type == "dimension" else fact_configs
    eligible_configs = filter(lambda cfg: cfg["name"] == conf_name, conf_list)
    assert(len(eligible_configs) == 1)
    cfg = eligible_configs[0]

    if conf_type == "dimension":
        return (conf_type,
                conf_name,
                run_dimension_etl(pygram_dimension_factory=cfg["dimension_handler"],
                                  source_conn=_source_conn,
                                  output_conn=_output_conn,
                                  source_sql=cfg["source_sql"],
                                  create_sql=cfg["create_sql"]))
    else:
        cached_dimensions = load_cached_dimensions(_output_conn)
        return (conf_type,
                conf_name,
                run_fact_etl(pygram_fact_factory=cfg["fact_handler"],
                             source_conn=_source_conn,
                             output_conn=_output_conn,
                             source_sql=cfg["source_sql"],
                             create_sql=cfg["create_sql"],
                             dimensions=cached_dimensions))

@celery.task(time_limit=43200)
def refresh_data_warehouse(run_dimensions=True, run_facts=True,
                           delete_existing_tables=True):
    print "Refreshing data warehouse."

    refresh_results = []

    if delete_existing_tables:
        delete_existing_dimensions_and_facts(_output_conn)

    if run_dimensions:
        etl_signature_list = [process_etl.s(d["name"], "dimension")
                              for d in dimension_configs if d["etl_active"]]

        etl_job = group(etl_signature_list)
        etl_job_result = etl_job.apply_async()
        return_vals = etl_job_result.get()  # This forces a wait

        if not etl_job_result.successful():
            # Consider an email here.
            raise Exception("Not all dimension ETL processes succeeded. Results=%s" %
                            (return_vals))
        else:
            refresh_results.append(return_vals)

    if run_facts:
        etl_signature_list = [process_etl.s(d["name"], "fact")
                              for d in fact_configs if d["etl_active"]]
        etl_job = group(etl_signature_list)
        etl_job_result = etl_job.apply_async()
        return_vals = etl_job_result.get()  # This forces a wait
        if not etl_job_result.successful():
            # Consider an email here.
            raise Exception("Not all fact ETL processes succeeded. Results=%s" %
                            (return_vals))
        else:
            refresh_results.append(return_vals)
    print refresh_results
    return refresh_results



# To deploy the nightly job assign this to the config variable
# CELERYBEAT_SCHEDULE in the file celeryconfig.py.
# We want to process at midnight East Coast time.  The current
# hour parameter must be adjusted at DST changeover.
NIGHTLY_REFRESH_SCHEDULE = {
        'data-warehouse-nightly-refresh': {
            'task': 'tasks.refresh_data_warehouse',
            'schedule': crontab(hour=4, minute=0),
            'args': (True, True, True)
    },
}
