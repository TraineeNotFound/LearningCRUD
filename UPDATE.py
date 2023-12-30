import mysql.connector


# Função para atualizar dados em uma tabela do banco de dados
def atualizar_dados(conexao, tabela, novos_valores, condicao=''):
    try:
        cursor = conexao.cursor()

        # Monta a parte SET da query de atualização com os novos valores a serem atualizados
        sets = ', '.join([f"{campo} = %s" for campo in novos_valores.keys()])
        consulta = f"UPDATE {tabela} SET {sets}"                # Monta a query de atualização

        if condicao:
            consulta += f" WHERE {condicao}"                    # Adiciona uma cláusula WHERE, se fornecida

        cursor.execute(consulta, list(novos_valores.values()))  # Executa a query de atualização com os novos valores

        conexao.commit()        # Realiza o commit para efetivar a atualização no banco de dados

        return cursor.rowcount  # Retorna o número de linhas afetadas pela operação de atualização

    except mysql.connector.Error as error:
        # Em caso de erro, imprime uma mensagem de erro e reverte a transação
        print(f"Erro ao atualizar dados no banco de dados: {error}")
        conexao.rollback()  # Reverte as alterações feitas na transação em caso de erro
        return None         # Retorna 'None' para indicar que a atualização não foi bem-sucedida
