dividendo = 10
divisor = 2
quociente = 0
resto = 0

resto = dividendo % divisor
quociente = dividendo / divisor

print(f"Dividendo {dividendo} com o divisor {divisor} tera o quociente: "
      f"{quociente}.")
print(f"Dividendo {dividendo} com o divisor {divisor} tera o resto: {resto}.")

if resto == 0:
    print("O número é positivo!")
else:
    print("O número é negativo!")
