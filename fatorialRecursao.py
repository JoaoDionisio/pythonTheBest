
def fatorialSemRecursao(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial


def fatorialRecursivo(numero):
    if numero == 0:  # CRITÉRIO DE PARADA.
        return 1
    else:
        # PARÂMETRO DE CHAMADA RECURSIVA
        return numero * fatorialRecursivo(numero - 1)


print(fatorialSemRecursao(5))
print(fatorialRecursivo(5))
