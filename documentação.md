# Documentação Técnica - Web Scraping de Séries

## 1. Visão Geral

Este projeto implementa um script de web scraping em Python para coletar informações sobre séries de um site específico (`https://nahoradoocio.lowlevel.com.br/category/maratonas-de-series/`). Os dados coletados (título e link da série) são então armazenados em um banco de dados PostgreSQL.

## 2. Estrutura do Projeto

A estrutura do projeto é composta por um único arquivo Python:

```
web-scraping/
├── web-scraping.py             # Script principal de web scraping
```

## 3. Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **`requests`**: Biblioteca para fazer requisições HTTP.
*   **`BeautifulSoup4` (`bs4`)**: Biblioteca para parsing de HTML e XML.
*   **`psycopg2`**: Adaptador PostgreSQL para Python, utilizado para interagir com o banco de dados.
*   **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional.

## 4. Funcionalidades Principais

O script `web-scraping.py` realiza as seguintes operações:

*   **Configuração de Logs**: Utiliza a biblioteca `logging` para registrar informações sobre o processo de scraping.
*   **Conexão com Banco de Dados**: Estabelece uma conexão com um banco de dados PostgreSQL, utilizando parâmetros configuráveis (nome do DB, usuário, senha, host, porta).
*   **Criação de Tabela**: Verifica se a tabela `series` existe no banco de dados e a cria caso não exista. A tabela possui colunas para `id` (chave primária serial), `titulo` (VARCHAR) e `link` (VARCHAR).
*   **Web Scraping**: Itera sobre um número predefinido de páginas de uma categoria específica do site alvo.
    *   Faz requisições HTTP para cada página.
    *   Utiliza `BeautifulSoup` para analisar o conteúdo HTML.
    *   Extrai o título e o link de cada post de série.
*   **Inserção de Dados**: Insere os títulos e links das séries extraídas na tabela `series` do banco de dados.

## 5. Parâmetros Configuráveis

Os seguintes parâmetros podem ser ajustados diretamente no script:

*   **Parâmetros de Conexão com o Banco de Dados**:
    *   `dbname`: Nome do banco de dados (padrão: `web_scraping`)
    *   `user`: Usuário do banco de dados (padrão: `postgres`)
    *   `password`: Senha do usuário do banco de dados (padrão: `91881200`)
    *   `host`: Host do banco de dados (padrão: `localhost`)
    *   `port`: Porta do banco de dados (padrão: `5432`)
*   **Configurações de Scraping**:
    *   `base_url`: URL base do site a ser raspado (padrão: `https://nahoradoocio.lowlevel.com.br/category/maratonas-de-series/page`)
    *   `num_pages`: Número de páginas a serem raspadas (padrão: `2`)

## 6. Configuração e Execução

Para configurar e executar o projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   **Python 3.x**
*   **PostgreSQL**: Servidor de banco de dados instalado e configurado.

### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/rafaelcrb/web-scraping.git
    cd web-scraping
    ```
2.  Instale as dependências Python:
    ```bash
    pip install requests beautifulsoup4 psycopg2-binary
    ```

### Configuração do Banco de Dados

1.  Certifique-se de que seu servidor PostgreSQL esteja em execução.
2.  Crie um banco de dados com o nome especificado no script (`web_scraping` por padrão) e um usuário com as credenciais correspondentes, ou ajuste os parâmetros `dbname`, `user`, `password`, `host`, `port` no script `web-scraping.py` para corresponder à sua configuração de banco de dados.

### Execução

1.  Navegue até o diretório do projeto.
2.  Execute o script Python:
    ```bash
    python web-scraping.py
    ```
    O script irá se conectar ao banco de dados, criar a tabela (se necessário), realizar o scraping e inserir os dados. Mensagens de log serão exibidas no console.

## 7. Considerações de Desenvolvimento

*   O script utiliza `logging` para fornecer feedback sobre o processo.
*   A criação da tabela `series` é idempotente (`IF NOT EXISTS`), garantindo que o script pode ser executado múltiplas vezes sem erros de tabela já existente.
*   É importante notar que a estrutura de um site pode mudar, o que pode quebrar o seletor `find_all("article", class_="post")` ou a extração de `h2` e `a`.
*   Para um ambiente de produção, é recomendável externalizar as credenciais do banco de dados (por exemplo, usando variáveis de ambiente) e implementar um tratamento de erros mais robusto.


