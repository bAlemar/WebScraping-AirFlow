# AirFlow WebScraping

### Objetivo
Monitorar os preços de Placa de Video.

Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:

- Docker version 24.0.7
- docker-compose 1.29.2 (Linux)
- Python 3.10.12
- pip (gerenciador de pacotes Python)
- Git (ferramenta de controle de versão)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/WebScraping-AirFlow.git
2. **Navegue até o diretório do repositório clonado:**
   ```bash
   cd WebScraping-AirFlow/V2

4. **Buildar nosso Dockerfile (imagem extendida):**
   ```bash
   docker build . --tag exteding_airflow:latest 

6. **Definir alguns variáveis de ambiente(Linux):**
   ```bash
   echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env 

5. **Buildar o Docker-compose (onde contém aplicação airflow):**
   ```bash
   docker-compose up airflow-init
5. **OBS: Caso queira altera alguma dag e att o airflow basta:**
   ```bash
   docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler