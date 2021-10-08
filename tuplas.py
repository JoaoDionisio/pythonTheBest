from rich import print

tupla1 = (10, True, "Deus", "Jesus", "Holy")
(x, *y, z) = tupla1
print("x: ", x)
print("y: ", y)
print("z: ", z)
