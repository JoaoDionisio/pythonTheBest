"""
CÓDIGO PARA ADIVINHAR UM NÚMERO.

"""
palpite = 5
numero = 9

while True:
    print("Qual o número correto? ")
    palpite = int(input("Digite o número: "))
    if palpite == numero:
        print("Você acertou!")
        break
    else:
        print("Você não acertou. Tente outra vez. ")
