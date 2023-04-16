def fatorial(n):
    valor = n - 1
    while valor > 1:
        n = n * valor
        valor -= 1
    if n == 0:
        n = 1
    if n < 0:
        n = 0
    return n

import pytest

@pytest.mark.parametrize('entrada,saida', [
    (0,1),
    (1,1),
    (-10,0),
    (4,24),
    (5,120)])

def testa_fatorial(entrada, saida):
    assert fatorial(entrada) == saida

