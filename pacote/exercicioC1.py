rota01 = ['cidade01', 'cidade02', 'cidade03', 'cidade04', 'cidade05',
          'cidade06']
rota02 = ['cidade01', 'cidade02', 'cidade03', 'cidade07', 'cidade08',
          'cidade09', 'cidade10', 'cidade11', 'cidade12']
rota03 = ['cidade01', 'cidade02', 'cidade03', 'cidade13', 'cidade14',
          'cidade15', 'cidade16', 'cidade17', 'cidade18']

custoRota01 = 1200
custoRota02 = 1350
custoRota03 = 1650
rotaBarata01 = None
rotaBarata02 = None
rotaBarata03 = None
rotaMaisBarata = "rota"
consulta = True


def continuar(resposta):
    resposta = resposta.lower()
    if (resposta in 'sim'):
        return True
    return False


while(consulta):
    opcao01 = input('Qual a 1° cidade você deseja visitar? ')
    opcao02 = input('Qual a 2° cidade você deseja visitar? ')
    opcao01 = opcao01.lower()
    opcao02 = opcao02.lower()
    print(f"A sua primeira cidade escolhida foi {opcao01}.")
    print(f"A sua segunda cidade escolhida foi {opcao02}.")

    if (opcao01 in rota01) and (opcao02 in rota01):
        rotaBarata01 = True
    if (opcao01 in rota02) and (opcao02 in rota02):
        rotaBarata02 = True
    if (opcao01 in rota03) and (opcao02 in rota03):
        rotaBarata03 = True
    if (rotaBarata01 is False) and (rotaBarata02 is False) and \
            (rotaBarata03 is False):
        print('Não encontrado suas cidades.')

    if (rotaBarata01 is True):
        rotaMaisBarata = "rota01"
        print(f"A rota mais barata é a Rota 1 e o custo é {custoRota01}.")
    elif (rotaBarata02 is True):
        rotaMaisBarata = "rota02"
        print(f"A rota mais barata é a Rota 2 e o custo é {custoRota02}.")
    else:
        print(f"A única rota disponível encontrada foi a rota 3 e o"
              f" preço dela é {custoRota03}")

    consulta = continuar(input('Você deseja continuar? '))
    rotaBarata01 = None
    rotaBarata02 = None
    rotaBarata03 = None
    rotaMaisBarata = "rota"
else:
    print('Programa finalizado. boa viagem.')
