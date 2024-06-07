from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from scripts.upload_to_gcs import upload_files_to_gcs
from scripts.load_to_bigquery import load_files_to_bigquery

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='ETL pipeline to process CSV and Parquet files',
    schedule_interval=None,
)

upload_task = PythonOperator(
    task_id='upload_files_to_gcs',
    python_callable=upload_files_to_gcs,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_files_to_bigquery',
    python_callable=load_files_to_bigquery,
    dag=dag,
)

upload_task >> load_task
