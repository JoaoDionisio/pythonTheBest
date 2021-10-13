from rich import print

#  Pedra Papel e Tesoura - Game DANKI CODE
ordem = True


def opcao_jogador():
    opcao = input("Escolha Pedra, Papel ou Tesoura: ")
    opcao.lower()
    if opcao == "pedra":
        return opcao
    elif opcao == "papel":
        return opcao
    elif opcao == "tesoura":
        return opcao
    else:
        print("Você nao digitou umas das opções válidas.")
        opcao_jogador()


while ordem:

    opcao_jogador()

    esc_jogador = input("Você quer jogar novamente?")
    esc_jogador.lower()
    print(esc_jogador)

    if esc_jogador in "sim":
        print("Very well. Let's start again.")

    if esc_jogador in "naonão":
        ordem = False
        print(ordem)
