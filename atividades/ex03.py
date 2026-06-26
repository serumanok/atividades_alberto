def achatar_sem_comp(lista):
    res = []
    for item in lista:
        if isinstance(item, list):
            res.extend(achatar_sem_comp(item))
        else:
            res.append(item)
    return res

def achatar_com_comp(lista):
    return [item for sub in lista for item in (achatar_com_comp(sub) if isinstance(sub, list) else [sub])]

lista_ex = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]
print("Sem comp:", achatar_sem_comp(lista_ex))
print("Com comp:", achatar_com_comp(lista_ex))