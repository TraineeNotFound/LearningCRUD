import json
from decimal import Decimal
import mysql.connector


# Classe CustomEncoder para lidar com a serialização de objetos Decimal para JSON
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):  # Verifica se o objeto é do tipo Decimal
            return float(o)         # Converte Decimal para float para a serialização JSON
        return super().default(o)


# Função para consultar dados em uma tabela do banco de dados
def consultar_campos(conexao, tabela, campos, where_clause=''):
    try:
        cursor = conexao.cursor()

        # Verifica se todos os campos devem ser selecionados ou se há campos específicos a serem selecionados
        if campos == '*' or not campos:
            campos_str = '*'                # Se '*' for passado ou nenhum campo especificado, seleciona todos os campos
        else:
            campos_str = ', '.join(campos)  # Lista de campos convertida em string para a consulta SQL

        consulta = f"SELECT {campos_str} FROM {tabela}"     # Monta a consulta SQL básica

        if where_clause:
            consulta += f" WHERE {where_clause}"            # Adiciona uma cláusula WHERE à consulta, se fornecida

        cursor.execute(consulta)                            # Executa a consulta SQL

        if cursor.description:                              # Verifica se há resultados da consulta
            colunas = [i[0] for i in cursor.description]    # Obtém os nomes das colunas
            resultados = cursor.fetchall()                  # Obtém todos os resultados da consulta

            resultados_formatados = []
            for row in resultados:
                row_dict = dict(zip(colunas, row))          # Combina nomes de colunas com valores de uma linha

                if 'valor' in row_dict:
                    row_dict['valor'] = round(float(row_dict['valor']), 2)  # Arredonda e formata o valor para 2 casas decimais
                resultados_formatados.append(row_dict)                      # Adiciona o dicionário formatado à lista de resultados

            # Converte os resultados formatados em JSON, usando a classe CustomEncoder para lidar com Decimals
            resultados_json = json.dumps(resultados_formatados, cls=CustomEncoder, ensure_ascii=False)
            return resultados_json  # Retorna os resultados formatados em JSON
        else:
            return json.dumps([])   # Retorna uma lista vazia caso não haja resultados

    except mysql.connector.Error as error:
        print(f"Erro ao consultar o banco de dados: {error}")
        return None                 # Retorna 'None' em caso de erro na consulta ao banco de dados
