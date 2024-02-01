from conexao import criar_conexao
from SELECT import consultar_campos
from UPDATE import atualizar_dados
from INSERT import inserir_dados
from DELETE import deletar_dados


def main():
    conexao = criar_conexao('localhost', '3306', 'root', '****', 'python')

#   INÍCIO DO CRUD
# ------------------------------------------------------CREATE----------------------------------------------------------
#     dados_insercao = {
#         'nomeProduto': 'tênis',
#         'valor': 49.99
#     }
#     # Inserindo dados na tabela 'vendas'
#     resultado_insercao = inserir_dados(conexao, 'vendas', dados_insercao)
#
#     if resultado_insercao is not None:
#         print(f"Inserção bem-sucedida. Linhas afetadas: {resultado_insercao}")
#     else:
#         print("Falha ao inserir dados.")

# ------------------------------------------------------READ------------------------------------------------------------
#     resultado = consultar_campos(conexao, 'vendas', '*', '')
#     print("Resultado:")
#     print(resultado)

# ------------------------------------------------------UPDATE----------------------------------------------------------
#     novos_valores = {
#         'valor': 69.99
#     }
#     condicao = 'idVendas = 3'  # Condição para a atualização
#     resultado_atualizacao = atualizar_dados(conexao, 'vendas', novos_valores, condicao)
#
#     if resultado_atualizacao is not None:
#         print(f"Atualização bem-sucedida. Linhas afetadas: {resultado_atualizacao}")
#     else:
#         print("Falha ao atualizar dados.")

# ------------------------------------------------------DELETE----------------------------------------------------------
#     deletar_dados(conexao,'vendas','idVendas = 2')
# ----------------------------------------------------------------------------------------------------------------------
#   FIM DO CRUD

    conexao.close()


if __name__ == "__main__":
    main()
