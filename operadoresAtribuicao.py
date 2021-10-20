print("Receba 5 valores diferentes e diga qual é o maior e o menor.")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))


def maiorNumero(a, b, c, d, e):
    if a > b > c > d > e:
        print(f"A é o maior valor: {a}")
    elif b > c > d > e:
        print(f"B é o maior valor: {b}")
    elif c > d > e:
        print(f"C é o maior valor: {c}")
    elif d > e:
        print(f"D é o maior valor: {d}")
    else:
        print(f"E é o maior valor: {e}")


def menorNumero(a, b, c, d, e):
    if a < b < c < d < e:
        print(f"A é o menor valor: {a}")
    elif b < c < d < e:
        print(f"B é o menor valor: {b}")
    elif c < d < e:
        print(f"C é o menor valor: {c}")
    elif d < e:
        print(f"D é o menor valor: {d}")
    else:
        print(f"E é o menor valor: {e}")


maiorNumero(a, b, c, d, e)
menorNumero(a, b, c, d, e)
