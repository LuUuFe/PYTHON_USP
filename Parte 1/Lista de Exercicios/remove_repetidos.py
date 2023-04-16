def remove_repetidos(list):
    lista = []
    for item in list:
        if lista.count(item) == False:
            lista.append(item)
    return sorted(lista)
