lin = 0
col = 0


def linhaPrint(col):
    linha = []
    for i in range(col):
        linha.append(9)
    return linha


def printMatriz(matriz):
    matriz = matriz
    print(f"Lin: {lin}")
    print(f"Col: {col}")
    linha = linhaPrint(col)
    for i in range(lin):
        for j in range(col):
            linha[j] = matriz[i][j]
        print(linha)


def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        matriz.append(linha)
        #  print(matriz)
    return matriz


lin = int(input("Digite o número de linhas da matriz: "))
col = int(input("Digite o número de colunas da matriz: "))
linhaPrint(col)
m = cria_matriz(lin, col)
printMatriz(m)
