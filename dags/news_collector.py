from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from plugins.news_collection import get_news_data

# DATA EXTRACTION PHASE
# DAG arguments:
default_args = {
    'owner' : 'DainyNgyn',
    'depends_on_past':False,
    'start_date': datetime(2024, 10, 30),
    'email': ['dain55788@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries':'1',
    'retry_delay':timedelta(seconds=5),
    'catchup_by_default':False
}

# DAG Definition for News headlines collection:
dainy_dag = DAG(
    'simple_news_collector',
    description='Automatically collect news from NewsAPI and Transform',
    default_args=default_args,
    schedule_interval='@once', # daily 4AM UTC Timezone = 0AM NewYork Timezone
    tags=['news_collection'],
    catchup=False,
)

# Define Task
collect_news = PythonOperator(
    task_id='collect_news',
    python_callable=get_news_data,
    dag = dainy_dag
)

# Task Dependencies
collect_news
