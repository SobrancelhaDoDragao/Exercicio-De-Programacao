# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
from random import randint
from time import sleep
numero_sorteado = randint(0, 5)
chute_usuario = int(input("Adivinhe um numero de 1 à 5: "))

print("PROCESSANDO....")
#Esse comando faz o computador adormecer por um tempo.
sleep(1.5)
if chute_usuario == numero_sorteado:
    print("Parabéns você acertou!!")
else:
    print("Você errou!!")
