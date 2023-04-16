def computador_escolhe_jogada(n,m):
    multiplo = 1
    while n - (m + 1) * multiplo >= m and n - (m + 1) * multiplo > 0:
        if n - (m + 1) * multiplo > m:
            multiplo += 1
        else:
            return m
    if n - (m + 1) * multiplo < m and n - (m + 1) * multiplo > 0:
        return n - (m + 1) * multiplo
    elif n - (m + 1) * multiplo == 0:
        return m
    else:
        return n

def usuario_escolhe_jogada(n,m):
    valido = False
    while valido == False:
        pecas_retirada = int(input("\nQuantas peças você vai tirar? "))
        if pecas_retirada > m or pecas_retirada <= 0:
            print("\nOops! Jogada inválida! Tente de novo.")
        else:
            valido = True
            return pecas_retirada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    nao_tem_multiplo = False
    multiplo = 1
    while n != (m + 1) * multiplo and n > (m + 1) * multiplo and nao_tem_multiplo == False:
        multiplo += 1
    if n == (m + 1) * multiplo:
        nao_tem_multiplo = False
        print("\nVoce começa!")
    else:
        nao_tem_multiplo = True
        print("\nComputador começa!")        
    while n > 0:
        if nao_tem_multiplo == True:
            nao_tem_multiplo = False
            pecas_retirada_computador = computador_escolhe_jogada(n,m)
            n = n - pecas_retirada_computador
            if pecas_retirada_computador > 1:
                print("\nO computador tirou",pecas_retirada_computador,"peças.")
                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                else:
                    print("Agora restam",n,"peças no tabuleiro.\n")
            if pecas_retirada_computador == 1:
                print("\nO computador tirou uma peça.")
                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                else:
                    print("Agora restam",n,"peças no tabuleiro.\n")
        elif nao_tem_multiplo == False:
            nao_tem_multiplo = True
            pecas_retirada = usuario_escolhe_jogada(n,m)
            n = n - pecas_retirada
            if m == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("Voce tirou",pecas_retirada,"peças.")
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam",n,"peças no tabuleiro.\n")

def campeonato():
    modo = int(input("\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    if modo == 1:
        partida()
    if modo == 2:
        print("\nVoce escolheu um campeonato!")
        print("\n**** Rodada 1 ****\n")
        partida()
        print("\n**** Rodada 2 ****\n")
        partida()
        print("\n**** Rodada 3 ****\n")
        partida()
        print("\n**** Final do campeonato! ****\n")
        print("Placar: Você",0,"X",3,"Computador")

def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    campeonato()

main()