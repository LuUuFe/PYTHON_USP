valor = int(input("Digite um número: "))
lista = []
while valor > 0:
    lista.append(valor)
    valor = int(input("Digite um número: "))
lista.reverse()
for item in lista:
    print(item)
