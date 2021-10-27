"""Faça um programa que peça para o usuário digitar o nome e o salário
de vários funcionários e ao final o programa calcula e mostra o total
da folha  de pagamento. O programa acaba
quando o salário for -1."""

nomeFuncionarios = [""]
salarioFuncionarios = [0]
contador = 0
salarioTotal = 0.0

print(salarioFuncionarios[contador])
while(salarioFuncionarios[contador] != -1):
    nomeFuncionarios.append(input("Digite o nome do funcionário: "))
    salarioFuncionarios.append(float(input("Salário do funcionário? ")))
    if(salarioFuncionarios[contador] == -1):
        nomeFuncionarios.pop()
        break
    salarioTotal += salarioFuncionarios[contador]
    contador += 1

print(nomeFuncionarios)
print(salarioFuncionarios)
print(contador)
nomeFuncionarios.remove(nomeFuncionarios[contador])
nomeFuncionarios.remove(nomeFuncionarios[0])
salarioFuncionarios.remove(salarioFuncionarios[contador])
salarioFuncionarios.remove(salarioFuncionarios[0])

print(nomeFuncionarios)
print(salarioFuncionarios)
print(f"A folha de pagamento da empresa é: {salarioTotal}.")
