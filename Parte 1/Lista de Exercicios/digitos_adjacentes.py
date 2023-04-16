valor = int(input("Digite um número inteiro: "))
div_inteira = 1
soma = 0
sim = False
while valor >= div_inteira:
    soma1 = (valor // div_inteira)%10
    div_inteira = div_inteira*10
    if soma1 == (valor // div_inteira)%10:
        print("sim")
        sim = True
if sim == False:
    print("não")