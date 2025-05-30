import logging
import requests
from bs4 import BeautifulSoup
import psycopg2

# Configuração de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Parâmetros de conexão com o banco de dados PostgreSQL
dbname = 'web_scraping'
user = 'postgres'
password = '91881200'
host = 'localhost'
port = '5432'

# Cria a conexão com o banco de dados
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Cria um cursor para executar comandos SQL
cur = conn.cursor()

# Define o comando SQL para criar a tabela de séries, se ela ainda não existir
create_table_query = '''
CREATE TABLE IF NOT EXISTS series (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR,
    link VARCHAR
)
'''

# Executa o comando SQL para criar a tabela
cur.execute(create_table_query)

# Commit das alterações (no caso de criação da tabela)
conn.commit()

# Configurações para scraping
base_url = "https://nahoradoocio.lowlevel.com.br/category/maratonas-de-series/page"
STATUS_OK = 200
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
num_pages = 2

# Função para inserir dados de uma série no banco de dados
def insert_serie(titulo, link):
    insert_query = "INSERT INTO series (titulo, link) VALUES (%s, %s)"
    cur.execute(insert_query, (titulo, link))
    conn.commit()

# Log de início
logging.info('Iniciando o scraping...')

# Itera sobre as páginas e insere os dados das séries no banco de dados
for num_page in range(1, num_pages + 1):
    url = f'{base_url}/{num_page}'
    response = requests.get(url, headers=headers)

    if response.status_code == STATUS_OK:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        posts = soup.find_all("article", class_="post")

        for post in posts:
            titulo = post.find("h2", class_="post-title").get_text().strip()
            link_titulo = post.find("h2", class_="post-title").find('a').get("href")
            
            # Insere os dados da série no banco de dados
            insert_serie(titulo, link_titulo)

# Log de finalização
logging.info('Scraping finalizado.')

# Fecha o cursor e a conexão com o banco de dados
cur.close()
conn.close()
