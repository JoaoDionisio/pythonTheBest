from rich import print

#  FUNÇÃO COM 3 PARÂMETROS OBRIGATÓRIOS.


def imprimir_nome(nome, sobrenome, idade):
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Idade: {idade}")


#  PARÂMETROS NOMEADOS
imprimir_nome(sobrenome="Lucena", nome="Prince", idade=2)
