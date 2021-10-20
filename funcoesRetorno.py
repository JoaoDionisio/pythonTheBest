from rich import print

# even odd


def par_impar():
    numero = 5000
    if (numero % 2) == 0:
        return "O número é par."
    return "O número é ímpar."  # Do you see? I don't need one else here.


print(par_impar())
