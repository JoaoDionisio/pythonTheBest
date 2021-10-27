numVotosA = numVotosB = numeroEleitores = 0
candidato = ""

numeroEleitores = int(input("Quantos eleitores?"))

for x in range(1, numeroEleitores+1):
    candidato = input("Qual o seu candidato?")
    if (candidato == "candidatoA"):
        numVotosA += 1
    else:
        numVotosB += 1

print(f"O candidato A teve {numVotosA} votos.")
print(f"O candidato B teve {numVotosB} votos.")
