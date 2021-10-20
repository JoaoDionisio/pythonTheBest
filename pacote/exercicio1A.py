# DECLARACAO DE VARIAVEIS
salarioBruto = salarioLiquido = 0
condicaoParada = ''
app = True


def valor_valido(x):
    if x > 0.0:
        print('Valor válido.')
        return True
    return False


def continuar(x):
    x = x.lower()
    if x in 'sim':
        return True
    else:
        return False


while(app):
    try:
        salarioBruto = float(input('Informe o seu salário 	bruto: '))
    except BaseException:
        print('Você digitou um valor errado. Digite novamente.')
        pass

    if (valor_valido(salarioBruto) is True):
        if (salarioBruto < 5000):
            print('O desconto será de 5%')
            salarioLiquido = salarioBruto * 0.95
        elif (salarioBruto < 8000):
            print('O desconto será de 7%')
            salarioLiquido = salarioBruto * 0.93
        else:
            print('O desconto será de 9%')
            salarioLiquido = salarioBruto * 0.91
    print('O seu salário líquido é: ', salarioLiquido)
    salarioBruto = salarioLiquido = 0
    condicaoParada = input('Você deseja continuar: ')
    app = continuar(condicaoParada)

else:
    print('Programa finalizado.')
