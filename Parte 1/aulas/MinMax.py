def MinMax(temp):
    print("A menor temperatura do mês foi:", minima(temp), "C.")
    print("A maior temperatura do mês foi:", maxima(temp), "C.")

def minima(temps):
    minimo = 0
    i = 0
    while i < len(temps):
        if temps[i] < minimo:
            minimo = temps[i]
        i += 1
    return minimo

def maxima(temps):
    maxima = 0
    i = 0
    while i < len(temps):
        if temps[i] > maxima:
            maxima = temps[i]
        i += 1
    return maxima
