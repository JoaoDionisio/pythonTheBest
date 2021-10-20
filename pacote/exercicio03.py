
a = float(input("Informe o primeiro valor: "))
b = float(input("Informe o segundo valor: "))
c = float(input("Informe o terceiro valor: "))

if(a > b and a > c):
    print("O maior valor é :", a)
elif(b > a and b > c):
    print("O maior valor é :", b)
elif(c > a and c > b):
    print("O maior valor é :", c)
else:
    print("Todos os valores informados são iguais.")
