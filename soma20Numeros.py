print("Receba 20 números, some-os e mostre o valor.")
x = a = b = 0

for i in range(1, 5):
    a = float(input(f"Digite o numerador da {i} fração a ser somada: "))
    b = float(input(f"Digite o denominador da {i} fração a ser somada: "))
    while b == 0:
        print("Digite um novo valor para b, pois zero não é um valor válido: ")
        b = float(input(f"Digite o denominador da {i} fração a ser somada: "))
    x += a / b
print(f"O valor da soma total é {x}.")
