n = int(input("Digite o valor de n: "))
valor = 1
novo_valor = 1
while valor <= n:
    if novo_valor % 2 != 0:
        print(novo_valor)
        novo_valor += 1
        valor += 1
    else:
        novo_valor += 1