def maior_primo(valor):
    divisor = 2
    while valor > divisor:
        if valor != divisor and valor % divisor == 0:
            valor -= 1
            divisor = 2
        divisor += 1
    return valor
