def imprime_matriz(matriz):
    i = 0
    j = 0
    while i < len(matriz):
        while j < len(matriz[0]):
            if j == len(matriz[0]) - 1:
                print(matriz[i][j], end = "")
            else:
                print(matriz[i][j], end = " ")
            j += 1
        print()
        i += 1
        j = 0
