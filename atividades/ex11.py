notas = list(map(int, input().split()))
print(len([n for n in notas if n > 5]))