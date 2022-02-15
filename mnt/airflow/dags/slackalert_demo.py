# Need to show 5 dags doing variety of tasks using a connection to db 
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os
import psycopg2 as pg
import sqlalchemy
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.hooks.base_hook import BaseHook
from airflow.operators.bash import BashOperator
import pandas as pd
from airflow.sensors.filesystem import FileSensor
from airflow.models import Variable

def task_fail_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection('slack_conn').password
    slack_msg = """
            :red_circle: Task Failed. 
            *Task*: {task}  
            *Dag*: {dag} 
            *Execution Time*: {exec_date}  
            *Log Url*: {log_url} 
            """.format(
            task=context.get('task_instance').task_id,
            dag=context.get('task_instance').dag_id,
            ti=context.get('task_instance'),
            exec_date=context.get('execution_date'),
            log_url=context.get('task_instance').log_url,
        )
    failed_alert = SlackWebhookOperator(
        task_id='slack_test',
        http_conn_id='slack_conn',
        webhook_token=slack_webhook_token,
        message=slack_msg,
        channel="#airflow_monitoring",
        username='airflow')
    return failed_alert.execute(context=context)

default_args = {
    'owner': 'sundar',
    'start_date': '2022-01-01',
    'on_failure_callback': task_fail_slack_alert
}



def _get_message() -> str:
    return "Hi from airflow"



slackalert_demo = DAG(
    'slackalert_demo',
    default_args=default_args,
    description='Slackalert Dag Demonstration',
    schedule_interval=timedelta(days=1),
    catchup=False
)



task_1 =BashOperator(task_id='error_handle_check_fail', bash_command='exit 1',dag=slackalert_demo)

task_2 =BashOperator(task_id='error_handle_check_success', bash_command='exit 0',dag=slackalert_demo)



