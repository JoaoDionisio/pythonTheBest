from rich import print


def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None):
    print(f"Título: {nomeImovel}")
    print(f"Número de quartos: {n_quartos}")
    if vagasGaragem is not None:
        print(f"Número de vagas: {vagasGaragem}")


print("***"*30)
imprimir_imovel("Casa para 3 pessoas - SP", 3, 2, 5)
