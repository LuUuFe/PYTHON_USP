def menor_nome(nomes):
    menor_nome = ''
    for nome in nomes:
        nome = nome.strip()
        if len(nome) < len(menor_nome) or menor_nome == '':
            menor_nome = nome.capitalize()
    return menor_nome
        
