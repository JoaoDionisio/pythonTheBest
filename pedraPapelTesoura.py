from rich import print

#  Pedra Papel e Tesoura
ordem = True

while ordem:
    esc_jogador = input("Você quer jogar novamente?")
    esc_jogador = esc_jogador.lower()
    print(esc_jogador)
    if esc_jogador in "sim":
        print("Very well. Let's go start.")

    if esc_jogador in "nao":
        ordem = False
        print(ordem)
