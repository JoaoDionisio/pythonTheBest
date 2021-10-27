""" Elabore um algoritmo onde sejam digitados três números e o programa
 mostra os três números na ordem crescente.
 Insira a resposta abaixo."""

a = b = c = 0

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if (a < b < c):
    print(f"{a} {b} {c}")
elif (a < c < b):
    print(f"{a} {c} {b}")
elif (b < a < c):
    print(f"{b} {a} {c}")
elif (b < c < a):
    print(f"{b} {c} {a}")
elif (c < a < b):
    print(f"{c} {a} {b}")
elif (c < b < a):
    print(f"{c} {b} {a}")
