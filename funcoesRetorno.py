from rich import print


def par_impar():
    numero = 5000
    if (numero % 2) == 0:
        return "O número é par."
    return "O número é ímpar."


print(par_impar())
