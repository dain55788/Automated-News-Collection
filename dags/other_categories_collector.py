from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from plugins.other_categories import get_other_news_categories
from airflow.utils.task_group import TaskGroup

categories_list = ['technology', 'sports', 'entertainment', 'politic', 'business', 'health']

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

# # DAG Definition for other categories news collection:
# other_categories_dag = DAG(
#     'other_categories_news_collector',
#     description='Collect weekly news of other news categories (sport, technology, health, politic, entertainmnet, ...)',
#     default_args=default_args,
#     schedule_interval='@weekly', # weekly schedule according to UTC timezone
#     tags=['other_news_categories_collection'],
#     catchup=False,
# )

# # Define task
# collect_other_categories = PythonOperator(
#     task_id='collect_other_categories_news',
#     python_callable=get_other_news_categories,
#     dag = other_categories_dag
# )

# # Task Dependencies:
# collect_other_categories

with DAG(
    'other_categories_news_collector',
    description='Collect weekly news of other news categories (sport, technology, health, politic, entertainmnet, ...)',
    default_args=default_args,
    schedule_interval='@once', # weekly schedule according to UTC timezone
    tags=['other_news_categories_collection'],
    catchup=False,
) as other_categories_dag:
    with TaskGroup("Category") as group:
        for category in categories_list:
            crawl_task = PythonOperator(
            task_id=f'collect_categories_{category}',
            python_callable=get_other_news_categories,
            # provide_context=True,
            op_kwargs={
                "category": category
            }
        )