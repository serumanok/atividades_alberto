def descendentes(arvore):
    filhos = arvore[1]
    return filhos + [d for filho in filhos for d in descendentes(filho)]

exemplo = ["A", [["B", []], ["C", [["D", []]]]]]
print(f"Descendentes: {descendentes(exemplo)}")