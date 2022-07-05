from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from lambda_function import lambda_execute
#import boto3


default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2022, 7, 4),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG("lambda_function",default_args=default_args, schedule_interval="@daily", catchup=False) as dag:
    t1=PythonOperator(task_id="lambda_function", python_callable=lambda_execute)