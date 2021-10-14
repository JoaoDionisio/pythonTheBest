from rich import print


def olaMundo():
    print("Olá mundão.")
    olaMundo()  # Loop infinito. Cuidado.
    print("Olá mundão.")


olaMundo()
