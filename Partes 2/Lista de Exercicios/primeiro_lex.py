def primeiro_lex(lista):
    primeiro = ' '
    for item in lista:
        if ord(item[0]) < ord(primeiro[0]) or primeiro == ' ':
            primeiro = item
    return primeiro
