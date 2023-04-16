def soma_lista(lista, soma=0, max=None):
    if max == None:
        max = len(lista)
    if max < 1:
        return soma
    else:
        soma += lista[max - 1]
        return soma_lista(lista,soma,max-1)
print(soma_lista([1,2,3,4,5,2]))