# Jogo do Nim:

# Um programa escrito em linguagem Python que permite um usuário jogar o NIM contra o computador.
# Script desenvolvido apartir do módulo 6 do curso "Introdução à Ciência da Computação com Python Parte 1".


# ----------------------- 1. Escolher jogada -----------------------
# 1.1 Computador: Para escolher um valor de retirada, deve-se aplicar
# uma estratégia explicada no exercício proposto.

# Estrátegia utilizada: O computador para ganhar precisa sempre deixar
# um número de peças que seja múltiplo de (m + 1) para o jogador. Caso
# isso não seja possível, o computador deve retirar o número máximo 
# possível do limite proposto.

def computador_escolhe_jogada(n, m):
    # Neste laço de repetição, ele irá conferir se os valores no intervalo limite são múltiplos de (m + 1)
    for i in range(1, m+1):
        if (n - i) % (m + 1) == 0:
            return i  
    # Caso ele não encontre, irá ser retornado o valor máximo
    return n  

# 1.2 Usuário: Nesta função, o usuário terá que escolher algum valor de retirada
# que esteja no intervalo estabelecido. Caso ele ultrapasse este valor, uma mensagem
# presente na linha 34 será retornada ao terminal.

def usuario_escolhe_jogada(n, m):
    while True:
        escolha = int(input("Quantas peças você vai tirar? "))
        if escolha > m:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            break
    return escolha


# ----------------------- 2. Inicializaçõo -------------------------
# 2.1 - Partida: Nesta opção o usuário irá jogar um único round com o computador.

# Esta função é a mais importante do programa, pois independente de sua inicialização
# ela será constantemente utilizada.

# Para indicar qual das entidades irão começar o jogo, segue abaixo as recomendações
# que fazem parte da estratégia de vitória para o computador: 

#   Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
#   Caso contrário, o computador toma a iniciativa de começar o jogo, declarando "Computador começa!"

def partida():

    # Essas variáveis são responsáveis por indicar o vencedor do jogo. 
    jogador_ganhou = False
    computador_ganhou = False

    n = int(input("Quantas peças? "))              # Número inicial de peças.
    m = int(input("Limite de peças por jogada? ")) # Número limite de retirada das peças.
    
    # Para identificar se um número é múltiplo do outro, chamamos o operador % (resto de divisão), 
    # pois se retornar 0 o valor de n será um múltiplo.
    if n % (m + 1) == 0:
        print("\nVocê Começa!\n")

        while n != 0:
            jogada = usuario_escolhe_jogada(n, m)

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if jogada == 1:
                n = n - jogada
                print("\nVocê tirou uma peça.")
            elif jogada > 1:
                n = n - jogada
                print(f"\nVoce tirou {jogada} peças.")

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            
            # Confere se não há peças no tabuleiro, pois caso não tenha o vencedor será a ultima entidade jogada, neste caso o usuário.
            if n == 0:
                jogador_ganhou = True
                break

            jogada = computador_escolhe_jogada(n, m)

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if jogada == 1:
                print("O computador tirou uma peça")
                n = n - jogada
            elif jogada > 1:
                print(f"O computador tirou {jogada} peças")
                n = n - jogada

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            
            # Confere se não há peças no tabuleiro, pois caso não tenha o vencedor será a ultima entidade jogada, neste caso o computador.
            if n == 0:
                computador_ganhou = True
                break

    else:
        print("\nComputador começa!\n")
        while n != 0:

            jogada = computador_escolhe_jogada(n, m)

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if jogada == 1:
                print("O computador tirou uma peça.")
                n = n - jogada
            elif jogada > 1:
                print(f"O computador tirou {jogada} peças")
                n = n - jogada

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")

            # Confere se não há peças no tabuleiro, pois caso não tenha o vencedor será a ultima entidade jogada, neste caso o computador.
            if n == 0:
                computador_ganhou = True
                break 

            jogada = usuario_escolhe_jogada(n, m)

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if jogada == 1:
                print("\nVocê tirou uma peça")
                n = n - jogada
            elif jogada > 1:
                print(f"\nvocê tirou {jogada} peças")
                n = n - jogada

            # Condicionais que irão concertar a saída de dados no singular e plural.
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")

            # Confere se não há peças no tabuleiro, pois caso não tenha o vencedor será a ultima entidade jogada, neste caso o usuário.
            if n == 0:
                jogador_ganhou = True
                break
    

    if jogador_ganhou:
        print("Fim do jogo! Você ganhou!")
        return 1    # Aqui, nós estamos retornando o valor de 1 para representar o Jogador. Isto se faz necessário para fazer o controle
                    #  de rounds no modo campeonato
    elif computador_ganhou:
        print("Fim do jogo! O computador ganhou!")
        return 0    # Aqui, nós estamos retornando o valor de 0 para representar o Computador. Isto se faz necessário para fazer o controle
                    #  de rounds no modo campeonato

# 2.2 - Campeonato: Nesta opção o usuário irá jogar um três rounds com o computador.

def campeonato():
    # Controla a quantidade de vitórias do Jogador/Computador
    placar_jogador = 0
    placar_computador = 0

    # Repete o jogo em até 3 rounds, como indicado no range:
    for i in range(3):
        print(f"\n**** Rodada {i+1} ****\n")
        vencendor = partida()
        if vencendor == 1:
            placar_jogador += 1
        elif vencendor == 0:
            placar_computador += 1
    
    # Imprime o placar de vitórias
    print("\n**** Final do campeonato! ****\n")

    print(f"Placar: Você {placar_jogador} X {placar_computador} Computador")

# ----------------- 3. Função principal do Script ----------------------

print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar uma campeonato "))

if(escolha == 1):
    print("\nVoce escolheu uma partida!")
    partida()
    print("")

elif(escolha == 2):
    print("\nVoce escolheu um campeonato!")
    campeonato()
