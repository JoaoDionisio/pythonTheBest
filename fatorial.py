# COMO ACHAR O FATORIAL DE UM NÚMERO

fatorial = 1

numero = int(input("Insira um número: "))

if numero < 0:
    print("O fatorial de números negativos não existe.")
elif numero == 0:
    print(f"O fatorial de {numero} é 1.")
else:
    for x in range(1, numero + 1):
        fatorial = fatorial * x
    print(f"O fatorial de {numero} é {fatorial}")
