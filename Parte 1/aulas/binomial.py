def fatorial(n):
    valor = n - 1
    while valor > 1:
        n = n * valor
        valor -= 1
    if n == 0:
        n = 1
    return n

def teste_fatorial():
    assert fatorial(0) == 1
def teste_fatorial():
    assert fatorial(1) == 1
def teste_fatorial():
    assert fatorial(2) == 2
def teste_fatorial():
    assert fatorial(3) == 6
def teste_fatorial():
    assert fatorial(4) == 24
    
