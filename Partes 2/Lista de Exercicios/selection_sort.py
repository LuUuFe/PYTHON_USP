def ordena(lista):
    seq = len(lista)
    for i in range(seq):
        menor_num = i
        for j in range(i + 1,seq):
            if lista[j] < lista[menor_num]:
                menor_num = j
        lista[menor_num], lista[i] = lista[i], lista[menor_num]
    return lista
            
