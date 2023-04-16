def maiusculas(frase):
    maiusculas = ''
    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <= 90:
            maiusculas += letra
    return maiusculas
