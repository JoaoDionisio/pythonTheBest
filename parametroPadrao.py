from rich import print


def imprimir_imovel(nomeImovel="Apart. SP", n_quartos=3, vagasGaragem=None,
                    *args):
    print(f"Título: {nomeImovel}")
    print(f"Número de quartos: {n_quartos}")
    if vagasGaragem is not None:
        print(f"Número de vagas: {vagasGaragem}")


def imprimir_nomes(*nomes):
    print(nomes)


print("***"*30)
lista = ["Ana", "Beatriz", "Pedro"]
imprimir_nomes(*lista)
