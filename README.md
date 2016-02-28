<h2>PypeLineETL</h2>

<h3>Introduction </h3>

This repo contains the code populating the Flashnotes Data Warehouse.  This system is comprised of lightweight ETL process management code that uses the opensource pygrametl package for some of the core dimensional modeling infrastructure.  Otherwise the codebase is a relatively pure pythonic ETL framework.  A few key design considerations

* Celery offers us a powerful means of executing ETLs asynchronously, but simple synchronous execution options are available from run.py

* Although our implementation uses MySql, it would be rather trivial to use Postgres or some other relational database management system.

* The system architecture maintains intentional decoupling between ETLs.  This allows for many powerful production configurations that exploit parallelization to its fullest.  For example, the ETLs could be spread out across several queues and task "workers" and indeed even accross multiple VMs.

Some general references on dimensional modeling and ETL management

[Dimensional Modeling Techniques](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)

[The Data Warehouse Toolkit (book)](http://www.amazon.com/The-Data-Warehouse-Toolkit-Dimensional/dp/0471200247)


<h3>System  Prerequisites</h3>

The repo [deploy](./deploy) subfolder contains two files [packages.txt](./deploy/packages.txt) and [requirements.txt](./deploy/requirements.txt)
which list the system package (obtained via brew or apt-get) and pip install packages respectively.


<h3>Basic ETL Workflow</h3>

![](http://www.gliffy.com/go/publish/image/7772209/M.png)

<h3>Overall System Organization</h3>

Pypline is currently designed for maximum configuration flexibility.  There are
really six files with which to be familiar in order to properly configure and deploy the system.

* config.py - describes which dimensions and facts are known to the system
* dimensions.py - pygram dimension object factory definitions
* facts.py - pygram fact object factory definitions
* sources.py - low level sql definitions for source tables
* creates.py - low level sql definitions for data warehouse tables
* tasks.py - asynchronous celery task definitions.


<h3>Synchronous Commandline Execution(using run.py) </h3>

For bootstrapping, test, or demonstration purposes it may be useful to simple run one or more etls from a command line.  Although in production a parallelized task management model is more suitable.  If you simply type `run.py` from the command line from within the main project folder Pypeline will execute any and all configured ETLs.  You can edit config.py to turn on and off any ETLs you don't wish to run.  In addition you can run `tests.py` which will validate that the source connections and queries are working for any configured ETLs.

<h5>Using run.py</h5>

This simple command line tool supports very basic arguments.  The organization of Pypeline encourages the user to use the various configuration files to govern which ETLs get run and what the various data sources are for each.  So in run.py there ar not complicated data connection parameters.  In addition there is no way to specify specific ETLs.

*Usage*

Enter `python run.py --help`

This will show you all of the available options

```
Usage: run.py [options]

Options:
  -h, --help
  --test_dimension_source  Test the dimensions source SQL queries (read-only)
  --run_dimensions         Run all active dimension ETLs
  --run_facts              Run all active fact ETLs
  --delete_existing_tables Delete all existing dimension and fact tables
```
NOTE: Only --test_dimensions_source defaults to True, so simply invoking `run.py` will run the dimension source tests.  This can be a good way to do basic environment validation.

<h3>Asynchronous Execution (using Celery)</h3>

The asynchronous task management is handled through Celery.  In tasks.py there are currently two celery tasks functions.  One is a lower level function which can execute a single ETL and the other is a higher level function which can run all configured ETLs as a group.  Furthermore the config.py ETL definitions can be used to turn an ETL on or off

<h5>System Prerequistes</h5>

As mentioned previously, it is necessary to have celery and redis configured to run the
ETL tasks in tasks.py.  A simple development setup can be run with the following invocations.  If you are running an AWS machine you may need to invoke these using sudo.

```
/usr/local/bin/redis-server &
/usr/local/bin/celeryd &
```


<h5>Task Running a Single ETL</h5> 

```
@celery.task
def process_etl(conf_name, conf_type)}}}
...
```

Run a single ETL (in a python shell)

```
In [2]: import tasks
In [3]: task = tasks.process_etl.apply_async(args=["school", "dimension"])
```

Check on the task status

```
In [4]: task.status
Out[4]: 'SUCCESS'

In [5]: task.result
Out[5]: ('dimension', 'user', 279)
```

Check the content of the school_dim Data Warehouse Table

```
mysql> select school_id, name, state from school_dim limit 3;
+-----------+------------------------------+-------+
| school_id | name                         | state |
+-----------+------------------------------+-------+
|       993 | Abilene Christian University | TX    |
|       995 | Academy of Art University    | CA    |
|       996 | Adams State College          | CO    |
+-----------+------------------------------+-------+
3 rows in set (0.00 sec)

```

<h5>Task Running a configured set of ETLs</h5> 

```
@celery.task
def refresh_data_warehouse(run_dimensions=True,
                           run_facts=True,
                           delete_existing_tables=True):
...
```

In this test configuration we have 4 dimension ETLs configured.  Let's run all of them (in a python shell) but let's skip running facts for now.

```
In [1]: import tasks

In [2]: task = tasks.refresh_data_warehouse.apply_async(args=[True, False, True])
```

Later we can check the task status. Note, that we have have status (updated row counts) for each of the 4 ETLs.

```
In [3]: task.status
Out[3]: 'SUCCESS'

In [4]: task.result
Out[4]: [[('dimension', 'product', 850),
  ('dimension', 'user', 279),
  ('dimension', 'course', 30418),
  ('dimension', 'date', 2191),
  ('dimension', 'school', 1687),
  ('dimension', 'payment_source', 3),
  ('dimension', 'disability_program', 1),
  ('dimension', 'affiliate', 4),
  ('dimension', 'site', 1)],
 []]
```

Now to get additional confirmation about what actually ran we can check run.log in etl-logs (output destination is configurable in config.py

```
INFO:__main__:Dropping table product_dim
INFO:__main__:Dropped table product_dim
INFO:__main__:Creating table product_dim.
INFO:__main__:Table product_dim created.
INFO:__main__:Executing source query for dimension product_dim
INFO:__main__:Loading data
INFO:__main__:Loaded 850 rows into table product_dim (elapsed time: 0:00:00.124727)
INFO:__main__:Dropping table user_dim
INFO:__main__:Dropped table user_dim
INFO:__main__:Creating table user_dim.
INFO:__main__:Table user_dim created.
INFO:__main__:Executing source query for dimension user_dim
INFO:__main__:Loading data
INFO:__main__:Loaded 279 rows into table user_dim (elapsed time: 0:00:00.046210)
INFO:__main__:Dropping table course_dim
INFO:__main__:Dropped table course_dim
INFO:__main__:Creating table course_dim.
INFO:__main__:Table course_dim created.
INFO:__main__:Executing source query for dimension course_dim
INFO:__main__:Loading data
INFO:__main__:Loaded 30418 rows into table course_dim (elapsed time: 0:00:03.141393)
INFO:__main__:Dropping table school_dim
INFO:__main__:Dropped table school_dim
INFO:__main__:Creating table school_dim.
INFO:__main__:Table school_dim created.
INFO:__main__:Executing source query for dimension school_dim
INFO:__main__:Loading data
INFO:__main__:Loaded 1687 rows into table school_dim (elapsed time: 0:00:00.167087)
```
