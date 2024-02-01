import mysql.connector


# Função para deletar dados de uma tabela do banco de dados
def deletar_dados(conexao, tabela, condicao=''):
    try:
        cursor = conexao.cursor()

        consulta = f"DELETE FROM {tabela}"  # Monta a query DELETE básica

        if condicao:
            consulta += f" WHERE {condicao}"    # Adiciona uma cláusula WHERE, se fornecida

        cursor.execute(consulta)    # Executa a query DELETE

        conexao.commit()            # Realiza o commit para efetivar a exclusão no banco de dados

        return cursor.rowcount      # Retorna o número de linhas afetadas pela operação de exclusão

    except mysql.connector.Error as error:
        # Em caso de erro, imprime uma mensagem de erro e reverte a transação
        print(f"Erro ao deletar dados do banco de dados: {error}")
        conexao.rollback()  # Reverte as alterações feitas na transação em caso de erro
        return None         # Retorna 'None' para indicar que a exclusão não foi bem-sucedida
