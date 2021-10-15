from rich import print


def imprimir_nome(nome, sobrenome, idade):
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Idade: {idade}")


sobrenome = "Lucena"
imprimir_nome(sobrenome=sobrenome, nome="Prince", idade=2)
