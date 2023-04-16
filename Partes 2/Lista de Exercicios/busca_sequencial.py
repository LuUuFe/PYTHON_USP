def busca(lista, elemento):
    seq = len(lista)
    for i in range(seq):
        for j in lista:
            if elemento == lista[i]:
                return i
    return False
