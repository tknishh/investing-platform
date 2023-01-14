from airflow.decorators import task, dag

from Helpers import *
import datetime
import configparser


# Configs
config = configparser.ConfigParser()
config.read('dags/pipeline.conf')
api_key = config.get('fixer_io_api_key', 'api_key')

# Initial dates to populate
start_date = '2022-01-01'
end_date = '2022-03-01'

# Setting default configs
default_args = {
    'start_date': datetime.date.fromisoformat(start_date)
}

# Dag #1 - Populating platform
@dag(dag_id='populating_platform', default_args=default_args, catchup=False, tags=['Initial_Load'])
def populate_platform():

    # task #1 - Extract rates from Fixer.io    
    @task()
    def task1_extract_rates():
        pass


# Instantiating the DAG
populate_platform = populate_platform()