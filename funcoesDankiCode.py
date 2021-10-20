from rich import print

# PARADIGMA IMPERATIVO --> TIPOS DE PROGRAMAÇÃO
# POO
# BLOCO EXTERNO

nome = "Python - variável global"  # VARIÁVEL GLOBAL


def minha_funcao():
    # BLOCO INTERNO --> corpo da Função
    nome = "Anna - variável local"  # variável local
    print(nome, "\n")


print("\n")
print(nome, "\n ")
minha_funcao()
