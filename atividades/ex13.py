matriz = [[1, 2], [3, 4, 6], [7, 8]]
print([n for linha in matriz for n in linha if n % 2 == 0])