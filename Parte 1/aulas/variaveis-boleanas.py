decrecente = True
anterior = int(input("Digite o primeiro número da sequencia: "))
valor = 1
while valor != 0 and decrecente:
    valor = int(input("Digite o número da sequência : "))
    if valor > anterior:
        decrecente = False
    anterior = valor
if decrecente:
    print("Decrescente")
else:
    print("Não está em ordem")