valor = int(input("Digite um número inteiro: "))
divisor = 2
naoprimo = True
while valor > divisor:
    if valor != divisor and valor % divisor == 0:
        print("não primo")
        naoprimo = False
        divisor = valor
    divisor += 1
if naoprimo != False and valor >= divisor:
    print("primo")
else:
    print("não primo")
