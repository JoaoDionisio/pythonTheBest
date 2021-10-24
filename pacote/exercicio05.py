"""Faça um programa que calcula a media de idade das meninas e a dos
meninos de um total de 5 alunos."""

contador = totalIdF = totalF = totalIdM = totalM = idade = 0
sexo = ""


while(contador < 5):
    sexo = input("Informe o sexo do adolescente: ")
    idade = int(input("Digite a idade do aluno(a):"))
    if sexo == "menina":
        totalIdF += idade
        totalF += 1
    else:
        totalIdM += idade
        totalM += 1
    contador += 1

print("A media das idades das meninas é: ", (totalIdF/totalF))
print("A media das idades dos meninos é: ", (totalIdM/totalM))
