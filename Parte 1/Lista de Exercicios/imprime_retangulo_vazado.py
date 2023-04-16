largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
x = 2
if altura == 2:
        print("#"*largura, end="\n")
        print("#"*largura, end="\n")
if altura == 1:
    print("#"*largura, end="\n")
while altura > x:
    print("#"*largura)
    while x < altura:
        print("#"," "*(largura - 4),"#")
        x += 1
    print("#"*largura)