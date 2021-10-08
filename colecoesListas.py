from rich import print

frase = "Hello world!"

for i in range(12):
    print(f"[on white][black][bold] {frase[i].upper()} [/][/][/]", end=" ")
