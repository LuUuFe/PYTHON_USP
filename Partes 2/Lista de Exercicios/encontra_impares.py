def encontra_impares(lista, imp=[], max=None):
    if max == None:
        max = len(lista)
    if max < 1:
        return imp
    else:
        if lista[max-1] % 2 != 0:
            imp.append(lista[max-1]) 
        return encontra_impares(lista,imp,max-1)
