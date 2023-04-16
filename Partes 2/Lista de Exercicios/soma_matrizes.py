def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        matriz = []
        i = 0
        j = 0
        while j < len(m1):
            coluna = []
            while i < len(m2[0]):
                coluna.append(m1[j][i] + m2[j][i])
                i += 1
            j += 1
            i = 0
            matriz.append(coluna)
    else:
        return False
    return matriz
