from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import pandas as pd
import requests 
import json

# Inserindo a pasta com as funções
import sys
sys.path.insert(0, '/usr/local/airflow')

# Funções
from Functions.Extract import webscraping_buscape
from Functions.Transform import *



with DAG(
    # Vamos passar os parâmetros
    # Id tem que ser um identificador único
    dag_id= 'dag_Teste',
    # Quando vai começar nosso Airflow
    start_date= datetime(2024,2,22),
    # Intervalo de tempo que nossa orquestração irá rodar
    schedule_interval='0 13 * * *',
    # A partir da nossa start_date até hoje, o catchup caso seja True, todos os dags que não foram executados serão executados a partir da criação de uma nova dag
    catchup=False
    # OBS: Airflow só será executado a partir start_date + schedule_interval
) as dag:


# Task WebScraping
    task_0_webscraping = PythonOperator(
        task_id = 'webscraping',
        python_callable= webscraping_buscape,
        provide_context=True
    )

#Task Tratativa Dados
    task_1_tratativa = PythonOperator(
        task_id = 'tratativa',
        python_callable=apply_transform,
        provide_context=True
    )

#Load dos dados na base de dados
    task_2_create = PostgresOperator(
        task_id = 'Criar_Tabela',
        postgres_conn_id = 'postgres-airflow',
        sql = """
            CREATE TABLE IF NOT EXISTS Placa_Video_Price (
                ID SERIAL PRIMARY KEY,
                data_hora TIMESTAMP,
                nome_item TEXT,
                preco REAL
                )
                """
    )

#Inserir os dados
    task_3_load = PostgresOperator(
        task_id = 'Input_dos_Dados',
        postgres_conn_id = 'postgres-airflow',
        sql = """
              
              """
    )
task_0_webscraping >> task_1_tratativa >> task_2_create >> task_3_load
