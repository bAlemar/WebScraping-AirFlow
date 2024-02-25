import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow import DAG
from airflow.operators.bigquery import BigQueryCreateEmptyTableOperator, BigQueryOperator, BigQueryQueryOperator
from airflow.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.transfers.gcs_tobigquery import GCSToBigQueryOperator

data_set_name = 'DataGlowUp'
with DAG(
    dag_id="dataglowup",
    default_args={"start_date": datetime.datetime.now()},
    schedule_interval=None,
) as dag:
    # Dummy strat task   
    start = DummyOperator(
        task_id='start',
        dag=dag,
    )

    task_0 = BigQueryCreateEmptyDatasetOperator(
        task_id = 'create_dataset_bq',
        dataset_id=data_set_name

    )

    # # Carregar dados do GCS para o BigQuery
    # task_1 = BigQueryCreateEmptyTableOperator(
    #     task_id="load_data",
    #     table_resource={
    #         "tableReference": {"tableId": "dataset.table"},
    #         "schema": [
    #             {"name": "column1", "type": "STRING"},
    #             {"name": "column2", "type": "INTEGER"},
    #         ],
    #     },
    #     source_format="CSV",
    #     source_uris=["gs://bucket/file.csv"],
    # )

    task_1 = GCSToBigQueryOperator(
        task_id = 'gcs_to_bq',
        bucket="dataglowup30",
        source_objects = [],
        destination_project_dataset_table=f"{data_set_name}/"
        schema_fields=[
            {'name':'event_time', 'type':'STRING','mode':'NULLABLE'},
            {'name':'event_type', 'type':'STRING','mode':'NULLABLE'},
            {'name':'product_id', 'type':'INTEGER','mode':'NULLABLE'},
            {'name':'category_id', 'type':'INTEGER','mode':'NULLABLE'},
            {'name':'category_code', 'type':'STRING','mode':'NULLABLE'},
            {'name':'brand', 'type':'STRING','mode':'NULLABLE'},
            {'name':'price', 'type':'FLOAT','mode':'NULLABLE'},
            {'name':'user_id', 'type':'INTEGER','mode':'NULLABLE'},
            {'name':'user_session', 'type':'STRING','mode':'NULLABLE'}
        ]
    )


    # # Tratar dados no BigQuery
    # task_2 = BigQueryOperator(
    #     task_id="treat_data",
    #     sql="""
    #     UPDATE dataset.table
    #     SET column1 = UPPER(column1);
    #     """,
    # )

    # # Unir tabelas e criar novo dataset
    # task_3 = BigQueryQueryOperator(
    #     task_id="join_tables",
    #     sql="""
    #     SELECT
    #         t1.column1,
    #         t2.column2
    #     FROM dataset.table1 AS t1
    #     INNER JOIN dataset.table2 AS t2
    #     ON t1.column1 = t2.column2;
    #     """,
    #     destination_dataset="new_dataset",
    # )

    task_0 >> task_1 >> task_2 >> task_3

