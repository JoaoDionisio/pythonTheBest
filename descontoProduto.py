nomeProduto = input("Qual o nome do seu produto? ")
precoProduto = float(input("Qual o preço do produto? "))
descontoProduto = float(input("Qual o valor do desconto? "))
descontoProduto = 1 - (descontoProduto/100)


def desconto(precoProduto, descontoProduto):
    return precoProduto * descontoProduto


precoComDesconto = desconto(precoProduto, descontoProduto)
print(precoComDesconto)
