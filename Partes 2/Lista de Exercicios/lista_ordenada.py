def ordenada(lista):
    seq = len(lista)
    ordenado = False
    if seq == 1:
        return True
    for i in range(seq - 1):
        for j in range(i + 1, seq):
            if lista[i] < lista[j]:
                ordenado = True
            else:
                return False
    return ordenado
