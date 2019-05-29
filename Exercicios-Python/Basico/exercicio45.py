# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
# Bugs: O computador não ganha e algumas vezes não existe if para situação
print("Jokenpô")
print(" ")

# Criando uma lista em python
jogadas = ['PAPEL', 'PEDRA', 'TESOURA']

# Jogo começa aqui
computador = choice(jogadas)

# O imput do jogador define o vetor das jogadas, que depois é salvo na variável jogador
jogador = jogadas[int(input("O jogo começou! digite 0 para PAPEL, 1 para PEDRA e 2 para TESOURA{} ".format(jogadas)))]
print(" ")

# Controlando a orden da jogadas
partida = [computador,jogador]

# Vendo que ganhou

# Primeiro todo os empates possíveis
if partida[0] == partida[1]:
    print("Empate! Computador jogou {} e jogador jogou {}.".format(computador,jogador))
# Agora todos as vitoria do computador
if partida[0] == 'PAPEL' and partida[1] == 'PEDRA':
    print("Computador ganhou! Papel enrola pedra.")
if partida[0] == 'PEDRA' and partida[1] == 'TESOURA':
    print("Computador ganhou! Pedra esmaga tesoura.")
if partida[0] == 'TESOURA' and partida[1] == 'PAPEL.':
    print("Computador ganhou! Tesoura corta papel.")
# Agora todas as vitorias do jogador
if partida[1] == 'PAPEL' and partida[0] == 'PEDRA':
    print("Jogador ganhou! Papel enrola pedra.")
if partida[1] == 'PEDRA' and partida[0] == 'TESOURA':
    print("Jogador ganhou! Pedra esmaga tesoura.")
if partida[1] == 'TESOURA' and partida[0] == 'PAPEL':
    print("Jogador ganhou! Tesoura corta papel.")
