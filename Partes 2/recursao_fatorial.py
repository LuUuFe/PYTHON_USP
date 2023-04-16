def fatorial(n):
    if n < 1:
        return 1  # base da recursão
    else:
        return n * fatorial(n-1)  # chamada recursiva

import pytest

@pytest.mark.parametrize("entrada, saida", [
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24),
    (5,120)])

def testa_fatorial(entrada, saida):
    assert fatorial(entrada) == saida
    
