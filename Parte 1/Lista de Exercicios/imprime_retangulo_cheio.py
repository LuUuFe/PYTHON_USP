largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
x = 1
if altura == x:
    print("#"*largura)
while altura > x:
    while x <= altura:
        print("#"*largura, end="\n")
        x += 1