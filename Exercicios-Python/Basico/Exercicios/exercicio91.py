'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
aleatórios. Guarde esses resultados em um dicionário. No final, coloque 
esse dicionário em ordem, sabendo que o vencedor tirou o maior número no 
dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

rank = dict()
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("\nValores sorteados: ")

for indice, jogador in jogadores.items():
    print(f"{indice} tirou {jogador} no dado.")
    sleep(1)

print("\nRanking dos jogadores: ")
i = 1
for jogador in rank:
    print(f"{i}ºlugar: {jogador}")
    i += 1
