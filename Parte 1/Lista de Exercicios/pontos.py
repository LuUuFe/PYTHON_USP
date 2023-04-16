import math
x1 = int(input("Digite o primeiro número: "))
y1 = int(input("Digite o segundo número: "))
x2 = int(input("Digite o terceiro número: "))
y2 = int(input("Digite o quarto número: "))
distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if distancia >= 10:
    print("longe")
else:
    print("perto")