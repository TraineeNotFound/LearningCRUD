import mysql.connector


# Função para inserir dados em uma tabela do banco de dados
def inserir_dados(conexao, tabela, dados):
    try:
        cursor = conexao.cursor()

        campos = ', '.join(dados.keys())            # Obtém os nomes dos campos para a inserção
        valores = ', '.join(['%s'] * len(dados))    # Prepara os marcadores de posição para os valores

        # Monta a query de inserção com os campos e marcadores de posição
        consulta = f"INSERT INTO {tabela} ({campos}) VALUES ({valores})"

        # Executa a query de inserção com os valores fornecidos
        cursor.execute(consulta, list(dados.values()))

        conexao.commit()    # Realiza o commit para efetivar a inserção no banco de dados

        return cursor.rowcount   # Retorna o número de linhas afetadas pela operação de inserção

    except mysql.connector.Error as error:
        # Em caso de erro, imprime uma mensagem de erro e reverte a transação
        print(f"Erro ao inserir dados no banco de dados: {error}")
        conexao.rollback()   # Reverte as alterações feitas na transação em caso de erro
        return None          # Retorna 'None' para indicar que a inserção não foi bem-sucedida
