#  from rich import print


def reduzirNumero(numero):
    if numero > 0:
        reduzirNumero(numero - 1)
        print(numero)


reduzirNumero(5)
