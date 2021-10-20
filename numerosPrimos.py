"""
DESCOBRIR SE UM NÚMERO É PRIMO!
"""
#  print(30 * "-")

#  numero = int(input("Insira um número para descobrir se o mesmo é primo."))


def numeroPrimo(numero):
    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                return "Não é primo."
        else:
            return "Este número é primo."
    else:
        return "Este número não é primo. Número menor ou igual a 1."


#  numeroPrimo(numero)
