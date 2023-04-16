def soma_hipotenusas(n):
    h = 1
    i = 1
    j = 1
    soma = 0
    valor = 0
    while h <= n:
        while i <= n:
            while j <= n:
                if i**2 + j**2 == h**2 and h != valor:
                    valor = h
                    soma = soma + h
                j += 1
            i += 1
            j = 1
        h += 1
        i = 1
        j = 1
    return soma