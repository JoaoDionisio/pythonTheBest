precoDolar = float(input("Qual o preço do dolar? "))
quantiaDolar = float(input("Você tem quantos dólares? "))
quantiaReal = float(input("Você tem quantos reais? "))


def converterDolarReal(dolar):
    return dolar * precoDolar


def converterRealDolar(quantiaReal):
    return quantiaReal / precoDolar


precoEmReais = converterDolarReal(quantiaDolar)
print(f"Você tem R${precoEmReais:.2f} reais")

precoEmDolar = converterRealDolar(quantiaReal)
print(f"Você tem ${precoEmDolar:.2f} dólares")
