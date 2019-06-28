"""
Faça um programa que ajude um jogador da Mega Sena a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
composta.
"""
from random import randint
from time import sleep

sorteio = []

print()
print('--'*30)
print("                   JOGO NA MEGA SENA   ")
print('--'*30)

numerodejogo = int(input("Quantos jogos vc quer? "))

for i in range(0, numerodejogo):
    sorteio = [randint(0, 60), randint(0, 60), randint(
        0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]

    for n in range(0, len(sorteio)):
        while sorteio.count(sorteio[n]) > 1:
            sorteio[n] = randint(0, 60)
    sorteio.sort()
    sleep(1)
    print(f"jogo {i}º{sorteio}")
