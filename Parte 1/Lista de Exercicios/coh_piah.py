import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))   

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    sentenca = re.split(r'[.!?,:;]+', sentenca)
    if sentenca[-1] == '':
        del sentenca[-1]
    return sentenca

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    frase = re.split(r'[.!?,:; ]+', frase)
    if frase[-1] == '':
        del frase[-1]
    return frase

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade = 0
    i = 0
    while i < len(as_a):
        similaridade = similaridade + (abs(as_a[i] - as_b[i]))
        i += 1
    return similaridade / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    
    palavras_separadas = separa_palavras(texto)
    sentencas_separadas = separa_sentencas(texto)
    frases_separadas = separa_frases(texto)
    
    soma_palavras = 0
    soma_caracteres_sentencas = 0
    soma_caracteres_frases = 0
    
    for palavra in palavras_separadas:
        soma_palavras = soma_palavras + len(palavra)
        
    for caracter in sentencas_separadas:
        soma_caracteres_sentencas = soma_caracteres_sentencas + len(caracter)
        
    for caracter in frases_separadas:
        soma_caracteres_frases = soma_caracteres_frases + len(caracter)
        
    assinatura.append(soma_palavras / len(palavras_separadas))
    assinatura.append(n_palavras_diferentes(palavras_separadas) / len(palavras_separadas))
    assinatura.append(n_palavras_unicas(palavras_separadas) / len(palavras_separadas))
    assinatura.append(soma_caracteres_sentencas / len(sentencas_separadas))
    assinatura.append(len(frases_separadas) / len(sentencas_separadas))
    assinatura.append(soma_caracteres_frases / len(frases_separadas))
    
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    probabilidade = 1
    i = 0
    lista_assinatura = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        compara = compara_assinatura(assinatura, ass_cp)
        lista_assinatura.append(compara)
    while i < len(lista_assinatura):
        assinatura_comparada = lista_assinatura[0]
        if lista_assinatura[i] < assinatura_comparada:
            probabilidade = i
        i += 1

    return probabilidade
            
            
        
        
    




















