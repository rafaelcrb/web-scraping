# Web Scraping de Séries

Um script Python para coletar informações sobre séries de um site e armazená-las em um banco de dados PostgreSQL.

## ✨ Funcionalidades

*   **Coleta de Dados**: Extrai títulos e links de séries de páginas web.
*   **Armazenamento em Banco de Dados**: Salva os dados coletados em uma tabela PostgreSQL.
*   **Logging**: Registra o progresso e informações importantes durante o scraping.

## 🚀 Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **`requests`**: Para requisições HTTP.
*   **`BeautifulSoup4`**: Para parsing de HTML.
*   **`psycopg2`**: Para interação com o PostgreSQL.
*   **PostgreSQL**: Banco de dados relacional.

## ⚙️ Instalação e Execução

Para rodar este projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   **Python 3.x**
*   **PostgreSQL**: Servidor de banco de dados instalado e configurado.

### Passos

1.  Clone o repositório:
    ```bash
    git clone https://github.com/rafaelcrb/web-scraping.git
    cd web-scraping
    ```
2.  Instale as dependências Python:
    ```bash
    pip install requests beautifulsoup4 psycopg2-binary
    ```
3.  **Configuração do Banco de Dados**:
    *   Certifique-se de que seu servidor PostgreSQL esteja em execução.
    *   Crie um banco de dados com o nome `web_scraping` (ou ajuste o nome no script `web-scraping.py`).
    *   O script irá criar a tabela `series` automaticamente.
4.  Execute o script Python:
    ```bash
    python web-scraping.py
    ```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


