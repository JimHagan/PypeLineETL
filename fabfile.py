
from fabric.api import env, run, cd, execute, prefix, put, task, sudo
from fabric.decorators import hosts
from fabric.colors import blue, green

env.user = "jim"
env.use_ssh_config = True

ENV_TYPE = "dev" # or "prod" or "beta", etc.

ETL_APP_DIR = '/opt/%s/fnetl/pypline' % ENV_TYPE
LOCAL_ENVIRON_FILE = './environ_%s.sh' % ENV_TYPE
ETL_HOST = ['ec2-54-197-51-113.compute-1.amazonaws.com']



@task
@hosts(ETL_HOST)
def update_etl_source(branch=None):
    """
        Update Data Warehouse ETL code
    """
    with cd(ETL_APP_DIR):
        run('git fetch', pty=False)
        if branch:
            print(blue('changing working dir to {}'.format(branch)))
            run('git checkout {}'.format(branch))
        else:
            current_branch = run("git rev-parse --abbrev-ref HEAD")
            print(blue('working on {}'.format(current_branch)))
        print(blue('pulling latest code changes'))
        run('git pull', pty=False)
        print(blue('installing updated python packages'))
        run('pip install -r deploy/requirements.txt')
        print(green('deployment complete!'))

@task
@hosts(ETL_HOST)
def create_data_warehouse_synchronous(environ_file,
                                      update_source=True,
                                      branch=None):
    """
     Build a complete data warehouse from scratch by executing run.py
    """
    if update_source:
        execute(update_etl_source, branch=branch)

    with cd(ETL_APP_DIR):
        print(blue('Running Data Warehouse Create (ENV_TYPE="%s")' % ENV_TYPE))
        put(LOCAL_ENVIRON_FILE, "../")
        sudo('source ../environ.sh') # source the file
        sudo('python run.py --run_dimensions --run_facts --delete_existing_tables')
        print (green('%s complete!' % "Dry run" if dry_run else "Update"))


