def bubble_sort(lista):
    fim = len(lista)
    for i in range(fim):
        primeiro = 0
        for j in range(primeiro + 1, fim):
            if lista[j] < lista[primeiro]:
                lista[j], lista[primeiro] = lista[primeiro], lista[j]
                print(lista)
            primeiro = j
    return lista
