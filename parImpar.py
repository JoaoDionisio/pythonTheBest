dividendo = 10
divisor = 2
quociente = 0
resto = 0

resto = dividendo % divisor
quociente = dividendo / divisor

print("Dividendo {} com o divisor {} tera o quociente: {}.".format(dividendo, divisor, quociente))
print("Dividendo {} com o divisor {} tera o resto: {}.".format(dividendo, divisor, resto))

if resto == 0:
    print("O número é positivo!")
else:
    print("O número é negativo!")
