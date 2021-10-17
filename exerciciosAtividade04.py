"""01 - Escreva um programa em que sejam lidos dois números reais, X e Y,
e sejam feitas chamadas a funções descritas abaixo, que deverão ser
implementadas. No escopo global deve ser impresso o resultado retornado
por estas funções. a) Uma função que receba X e Y como entrada e retorne
o maior deles;
b) Uma função que receba X e Y como entrada e retorne
   a média aritmética deles;"""

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if x > y:
    print(f"O maior valor é {x}")
else:
    print(f"O maior valor é {y}")

print(f"A média aritmética destes 2 elementos é {(x+y)/2}")

"""02 - Escreva uma função de potenciação, em que os dados de entrada são: base e
expoente (inteiros)."""


def pot(base, expoente):
    return base ** expoente


base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

print(pot(base, expoente))
