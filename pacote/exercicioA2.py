"""Faça um programa onde sejam digitados as três notas de um aluno e o programa
calcula a média dos alunos e mostra o resultado conforme o especificado
abaixo: Insira a resposta abaixo.
Media menor que 4.0  -> reprovado
Media de  4.0  a menor que 7.0  -> recuperação
Media maior que 7.0  -> aprovado"""

notas_alunoA = [0.0, 0.0, 0.0]
media = 0.0

# ENTRADA
for x in range(0, 3):
    notas_alunoA[x] = float(input(f"Digite a {x+1} nota:"))
    media += notas_alunoA[x]

# PROCESSAMENTO
media /= 3

# SAÍDA
if (media < 4):
    print(f"As notas do aluno são: {notas_alunoA}")
    print(f"A média do aluno foi: {media}. Reprovado.")
elif (media < 7):
    print(f"As notas do aluno são: {notas_alunoA}")
    print(f"A média do aluno foi: {media}. Recuperação.")
else:
    print(f"As notas do aluno são: {notas_alunoA}")
    print(f"A média do aluno foi: {media}. Parabéns. Aprovado.")
