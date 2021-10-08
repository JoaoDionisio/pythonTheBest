"""
DESCOBRIR SE UM NÚMERO É PRIMO!
"""
print(30 * "-")

numero = int(input("Insira um número para descobrir se o mesmo é primo."))

if numero > 1:
    for x in range(2, numero):
        if (numero % x) == 0:
            print("Não é primo.")
            break
    else:
        print("Este número é primo.")
