def ler_sequencia():
    entrada = input("Digite os números separados por espaço: ")
    return [int(x) for x in entrada.split()]

resultado = ler_sequencia()
print(f"Lista gerada: {resultado}")