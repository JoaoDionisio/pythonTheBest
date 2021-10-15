from rich import print

#  kwags imprime um dicionário.
def imprimir_nome(**nomes):
    print(f"Nome completo: {nomes['nome']} {nomes['sobrenome']} ")


imprimir_nome(nome="Ana", sobrenome="Linda")
