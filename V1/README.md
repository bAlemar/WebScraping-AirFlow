**Referência código airflow:**
 - video: https://www.youtube.com/watch?v=4DGRqMoyrPk&t=1356s


**Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:**

- Python 3.10.12
- pip (gerenciador de pacotes Python)
- Git (ferramenta de controle de versão)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/WebScraping-AirFlow.git
2. **Navegue até o diretório do repositório clonado:**
   ```bash
   cd WebScraping-AirFlow/V1

3. **Crie ambiente virtual e ativa(Linux)**
   ```bash
   python3 -m venv venv 
   source venv/bin/activate 

4. **Instalar as dependências**
   ```bash
   pip install –r requeriments.txt

5. **Definir pasta principal do AirFlow**
   ```bash
   export AIRFLOW_HOME=~/{path atual}
6. **Criação banco de dados do AirFlow (irá armazenar informações do workflow)**
   ```bash
   airflow db init
7. **Criação usuário**
   ```bash
   airflow users create \  

    --username admin \  

    --firstname Peter \  

    --lastname Parker \  

    --role Admin \  
8. **Executar agendamento dos dags( se não, não parece na interface do airflow)**
   ```bash
   airflow scheduler -D 