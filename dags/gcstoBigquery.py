# import os
# from airflow import DAG
# from airflow import models
# from airflow.providers.google.cloud.operators.bigquery import (
#     BigQueryCreateEmptyDatasetOperator,
#     BigQueryDeleteDatasetOperator,
#     BigQueryCreateEmptyTableOperator
# )
# from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
# from airflow.utils.dates import days_ago

# # project_id = 'vijay-project-01'
# DATASET_NAME = "sample_dataset"
# TABLE_NAME = "airflow_table"
# project_id='vijay-project-01'

# with DAG('example_gcs_to_bigquery',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:

#     load_csv = GCSToBigQueryOperator(
#         task_id='gcs_to_bigquery_example',
#         bucket='json_file_folder',
#         source_format='NEWLINE_DELIMITED_JSON',
#         source_objects='gs://json_file_folder',
#         destination_project_dataset_table=f"{project_id}.{DATASET_NAME}.{TABLE_NAME}",
#         gcp_conn_id ='google_cloud_default',
#         write_disposition='WRITE_TRUNCATE',
#         dag=dag,
#     )






import os
from airflow import DAG
from airflow import models
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryDeleteDatasetOperator,
)
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago
project_id = 'vijay-project-01'
DATASET_NAME = "From_airflow"
TABLE_NAME = "airflow_table"
dag = models.DAG(
    dag_id='new_gcs_to_bq_operator',
    start_date=days_ago(2),
    schedule_interval='@once',
    tags=['example'],
)
# create_test_dataset = BigQueryCreateEmptyDatasetOperator(
#     task_id='create_airflow_test_dataset', dataset_id=DATASET_NAME, dag=dag
# )
# [START howto_operator_gcs_to_bigquery]
schema = [
    {'name': 'discounted_price', 'type': 'STRING'}
]
load_csv = GCSToBigQueryOperator(
    task_id='gcs_to_bigquery_example',
    bucket='json_file_folder',
    gcp_conn_id ='google_cloud_default',
    source_objects='*.ndjson',
    source_format='NEWLINE_DELIMITED_JSON',
    create_disposition="CREATE_IF_NEEDED",
    schema_fields=schema,
    autodetect=True,
    write_disposition="WRITE_TRUNCATE",
    destination_project_dataset_table=f"{project_id}.{DATASET_NAME}.{TABLE_NAME}",
    dag=dag,
)



































# create_test_dataset = BigQueryCreateEmptyDatasetOperator(
#     task_id='create_airflow_test_dataset', 
#     gcp_conn_id='google-cloud-default',
#     project_id='vijay-project-01',
#     dataset_id=DATASET_NAME, 
#     dag=dag,

# )

# CreateTable = BigQueryCreateEmptyTableOperator(
#     task_id='BigQueryCreateEmptyTableOperator_task',
#     dataset_id='vijay-project-01.Airflow',
#     table_id='Employees',
#     project_id='vijay-project-01',
#     gcs_schema_object='gs://json_file_folder/file_1.ndjson',
#     gcp_conn_id='google-cloud-default',
#     google_cloud_storage_conn_id='google-cloud-default'
# )




# [START howto_operator_gcs_to_bigquery]








































# from datetime import datetime

# from airflow import DAG
# from airflow.decorators import task
# from airflow.operators.bash import BashOperator

# # A DAG represents a workflow, a collection of tasks
# with DAG(dag_id="demo", start_date=datetime(2022, 1, 1)) as dag:

#     # Tasks are represented as operators
#     hello = BashOperator(task_id="hello", bash_command="echo {{ conn.<google-cloud-default>.host }}")

#     @task()
#     def airflow():
#         print("airflow")

#     # Set dependencies between tasks
#     hello >> airflow()