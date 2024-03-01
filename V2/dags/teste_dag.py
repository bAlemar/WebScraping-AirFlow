from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

def get_requests():
    import requests
    print(f"Requestes: {requests.__version__}")


def get_beatiful():
    import bs4
    print(f"bs4: {bs4.__version__}")



with DAG(
    dag_id = 'teste_dependencies',
    start_date=datetime(2023,10,16)

) as dag:
    
    task_0 = PythonOperator(
        task_id = 'Requests',
        python_callable=get_requests

    )
    task_1 = PythonOperator(
        task_id = 'BeatifulSoup',
        python_callable=get_beatiful
    )

    task_0 >> task_1