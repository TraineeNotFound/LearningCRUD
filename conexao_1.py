import mysql.connector
import psycopg2

# Função para criar uma conexão com o banco de dados MySQL
def criar_conexao_mysql(host, port, user, password, database):
    try:
        # Tenta estabelecer a conexão com o banco de dados usando os parâmetros fornecidos
        conexao = mysql.connector.connect(
            host=host,            # Endereço do servidor do banco de dados
            port=port,            # Porta utilizada para a conexão (padrão: 3306 para MySQL)
            user=user,            # Nome de usuário para autenticação no banco de dados
            password=password,    # Senha do usuário para autenticação
            database=database     # Nome do banco de dados a ser acessado
        )
        return conexao  # Retorna a conexão estabelecida com sucesso

    except mysql.connector.Error as error:
        # Em caso de erro ao conectar, imprime uma mensagem de erro e retorna 'None' (nulo)
        print(f"Erro ao conectar ao banco de dados MySQL: {error}")
        return None   # Retorna 'None' indicando que a conexão não foi estabelecida com êxito
    
# Função para criar uma conexão com o banco de dados PostgreSQL
def criar_conexao_postgre(host, port, user, password, database):
    try:
        # Tenta estabelecer a conexão com o banco de dados usando os parâmetros fornecidos
        conexao = psycopg2.connect(
            host=host,          # Endereço do servidor do banco de dados
            port=port,          # Porta utilizada para a conexão (padrão: 5432 para PostgreSQL)
            user=user,          # Nome de usuário para autenticação no banco de dados
            password=password,  # Senha do usuário para autenticação
            dbname=database     # Nome do banco de dados a ser acessado
        )
        return conexao  # Retorna a conexão estabelecida com sucesso

    except psycopg2.Error as error:
        # Em caso de erro ao conectar, imprime uma mensagem de erro e retorna 'None' (nulo)
        print(f"Erro ao conectar ao banco de dados PostgreSQL: {error}")
        return None   # Retorna 'None' indicando que a conexão não foi estabelecida com êxito
