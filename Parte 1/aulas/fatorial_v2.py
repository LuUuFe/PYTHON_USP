n = 1
while n > 0:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        n = 1
    valor = n - 1
    while valor > 0:
        n = n * valor
        valor -= 1
    print(n)