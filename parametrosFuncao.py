from rich import print


def minha_funcao(nome=None):
    if nome is None:
        size = 0
    else:
        size = len(nome)
    print(f"Olá {nome}. O seu nome tem {size} letras.")


nome = input("Qual o seu nome: ")
minha_funcao(nome)
