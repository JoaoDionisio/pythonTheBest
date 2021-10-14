from rich import print
from random import choice  # From random import only function choice.

#  Pedra Papel e Tesoura - Game DANKI CODE
ordem = True
jogador_vitorias = 0
maq_vitorias = 0
empates = 0


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


def opcao_maquina():
    opcao = choice(["pedra", "papel", "tesoura"])
    return opcao


while ordem:

    print("[on white][bold][red]-[/][/][/]"*80)
    opcao_jog = opcao_jogador()
    opcao_maq = opcao_maquina()
    print("[on white][bold][red]-[/][/][/]"*80)

    if (opcao_jog == "pedra") and (opcao_maq == "tesoura")\
        or (opcao_jog == "papel") and (opcao_maq == "pedra")\
            or (opcao_jog == "tesoura") and (opcao_maq == "papel"):
        print(f"O Jogador escolheu: {opcao_jog} e a Máquina "
              f"escolheu: {opcao_maq}. Resultado: Você ganhou")
        jogador_vitorias += 1
    elif opcao_jog == opcao_maq:
        print(f"O Jogador escolheu: {opcao_jog} e a Máquina "
              f"escolheu: {opcao_maq}. Resultado: Empate.")
        empates += 1
    else:
        print(f"O Jogador escolheu: {opcao_jog} e a Máquina "
              f"escolheu: {opcao_maq}. Resultado: Máquina ganhou")
        maq_vitorias += 1

    print("[on white][bold][blue]-[/][/][/]"*50)
    print(f"O jogador tem {jogador_vitorias} vitória(s).")
    print(f"A máquina tem {maq_vitorias} vitória(s).")
    print(f"Número de empates: {empates}.")
    print("[on white][bold][blue]-[/][/][/]"*50)

    esc_jogador = input("Você quer jogar novamente?")
    esc_jogador.lower()
    print(esc_jogador)

    if esc_jogador in "sim":
        print("Very well. Let's start again.")

    if esc_jogador in "naonão":
        ordem = False
        print(ordem)
