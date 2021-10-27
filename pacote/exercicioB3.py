numVotosA = numVotosB = numeroEleitores = 0
branco = nulo = 0
candidato = ""
dict = {
    "x": "Candidato A",
    "y": "Candidato B",
    "b": "Voto branco",
    "n": "Voto nulo"
}

numeroEleitores = int(input("Quantos eleitores? "))

for x in range(1, numeroEleitores+1):
    for x in dict:
        print(f"Digite {x} para o {dict[x]}.")
    candidato = input("Qual o seu candidato?")
    candidato = candidato.lower()
    if (candidato in "x"):
        numVotosA += 1
    elif (candidato in "y"):
        numVotosB += 1
    elif (candidato in "b"):
        branco += 1
    else:
        nulo += 1
print(f"O candidato A teve {numVotosA} votos.")
print(f"O candidato B teve {numVotosB} votos.")
print(f"O numero total de votos brancos {branco}")
print(f"O numero total de votos nulos {nulo}")
