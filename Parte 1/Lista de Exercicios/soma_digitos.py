valor = int(input("Digite um número inteiro: "))
div_inteira = 1
div_restante = 10
soma = 0
while valor >= div_inteira:
    soma1 = (valor // div_inteira)%div_restante
    soma = soma + soma1
    div_inteira = div_inteira*10
print(soma)