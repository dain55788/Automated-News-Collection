from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from plugins.other_categories import get_other_news_categories
from plugins.data_transformation import transform_other_news

# Default Arguments
default_args = {
    'owner' : 'DainyNgyn',
    'depends_on_past':False,
    'start_date': datetime(2024, 10, 20),
    'email': ['dain55788@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries':'1',
    'retry_delay':timedelta(seconds=5),
    'catchup_by_default':False
}

# DAG Definition for other categories news collection:
other_categories_dag = DAG(
    'other_categories_news_collector',
    description='Collect weekly news of other news categories (sport, technology, health, politic, entertainmnet, ...)',
    default_args=default_args,
    schedule_interval='@weekly', # weekly schedule according to UTC timezone
    tags=['other_news_categories_collection'],
    catchup=False,
)

# Define task
collect_other_categories = PythonOperator(
    task_id='collect_other_categories_news',
    python_callable=get_other_news_categories,
    dag = other_categories_dag
)

# Data Transformation
news_transformation = PythonOperator(
    task_id='news_transformation',
    python_callable = transform_other_news,
    dag=other_categories_dag
)

# Task Dependencies:
collect_other_categories >> news_transformation
