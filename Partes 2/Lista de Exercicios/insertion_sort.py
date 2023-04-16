def insertion_sort(lista):
    fim = len(lista)
    for i in range(fim):
        primeiro = i
        for j in range(i + 1, fim):
            if lista[j] < lista[primeiro]:
                lista[j], lista[primeiro] = lista[primeiro], lista[j]
    return lista
