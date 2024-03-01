from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
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

task_0_webscraping >> task_1_tratativa

# def captura_conta_dados():
#     url = 'https://data.cityofnewyork.us/resource/rc75-m7u3.json'
#     response = requests.get(url)
#     df = pd.DataFrame(json.loads(response.content))
#     qtd = len(df.index)
#     return qtd

# # OBS como vamos pegar o valor de qtd que está em outra função?
# # Execom é função do Airflow conseguimos compartilha informações entre as tasks. Essa informação fica dentro do db do AirFlow
# # Task é uma ação isolada

# def e_valida(ti):
#     qtd = ti.xcom_pull(task_ids = 'captura_conta_dados')
#     if (qtd > 1000):
#         return 'valido'
#     return 'não_valido'
# # With para alocar recursos
# with DAG(
#     # Vamos passar os parâmetros
#     # Id tem que ser um identificador único
#     dag_id= 'dag_Teste',
#     # Quando vai começar nosso Airflow
#     start_date= datetime(2024,2,24),
#     # Intervalo de tempo que nossa orquestração irá rodar
#     schedule=None,
#     # A partir da nossa start_date até hoje, o catchup caso seja True, todos os dags que não foram executados serão executados a partir da criação de uma nova dag
#     catchup=False
#     # OBS: Airflow só será executado a partir start_date + schedule_interval
# ) as dag:
    
# # Se você vai usar task que vai utilizar o Python você vai criar com PythonOperator e assim vai.
# # Se você vai utilizar bash, você utilizar bashoperator por exemplo


#     # Task 
#     task_0_captura_conta_dados = PythonOperator(
#         task_id = 'captura_conta_dados',
#         # Função que você vai chamar
#         python_callable = captura_conta_dados
#     )

#     task_1_main = BranchPythonOperator(
#         task_id = 'validação',
#         python_callable = e_valida


#     )

#     task_1_valido = BashOperator(
#         task_id = 'valido',
#         bash_command= "echo Quantidade OK"
#     )
#     task_1_2_n_valido = BashOperator (
#         task_id = 'não_valido',
#         bash_command="echo Quantidade Inválida"
#     )

#     task_0_captura_conta_dados >> task_1_main >> [task_1_valido,task_1_2_n_valido]
    
#     # BranchPythonOperator: Vai verificar determian condição e apartir dessa condição ele vai pra um lugar e caso c.c vai para outra