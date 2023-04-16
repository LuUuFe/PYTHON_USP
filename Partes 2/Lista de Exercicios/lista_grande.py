import random
import time
def lista_grande(n):
    antes = time.time()
    lista = []
    for i in range(n):
        lista.append(random.randrange(n))
    depois = time.time()
    return lista
