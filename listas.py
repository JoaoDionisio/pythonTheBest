from rich import print

lista01 = ["Carro", " ", ",", "Moto", "Avião"]
lista02 = ["Caminhão", ",", " ", "Navio"]
lista01.extend(lista02)
print(lista01)
for i in lista01:
    if i == " ":
        lista01.remove(" ")
for i in lista01:
    if i == ",":
        lista01.remove(",")
texto = " ".join(lista01)
print(texto)
texto = "".join(lista01)
print(texto)
