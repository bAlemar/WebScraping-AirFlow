FROM apache/airflow:2.8.2
COPY requeriments.txt /requeriments.txt
# Copie a pasta Functions para o contêiner
COPY Functions /usr/local/airflow/Functions
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requeriments.txt