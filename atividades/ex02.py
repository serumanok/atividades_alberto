def descendentes(arvore):
    if not arvore[1]:
        return []
    
    return [filho[0] for filho in arvore[1]] + \
           [n for filho in arvore[1] for n in descendentes(filho)]

def descendentes_compreensao(arvore):
    return [
        pessoa
        for filho in arvore[1]
        for pessoa in [filho[0]] + descendentes(filho)
    ]

familia = ["Avô", [
    ["Pai", [
        ["Neto", []]
    ]],
    ["Tio", []]
    ]]

print(descendentes_compreensao(familia))