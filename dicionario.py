from rich import print

conjunto1 = {0, 2, 4, 6, 8}
conjunto2 = {0, 1, 3, 5, 7, 9}
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)
