def conta_letras(frase, contar = "vogais"):    
    quantidade = 0
    vogais = 'aeiouAEIOU '
    if contar == 'vogais':
        for vogal in vogais:
            for letra in frase:
                if letra == vogal and letra != ' ':
                    quantidade += 1
    elif contar == 'consoantes':
        quantidade = len(frase)
        for letra in frase:
            for vogal in vogais:
                if letra == vogal:
                    quantidade -= 1
    return quantidade
                     
