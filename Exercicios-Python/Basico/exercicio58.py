# Melhore o jogo do Exercicio 28 onde o computador vai 'pensar' em um numero entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer.
from random import randint
from time import sleep

numero_sorteado = randint(0, 5)
chute_usuario = int(input("Adivinhe um numero de 1 à 5: "))
tentativas = 1

print("PROCESSANDO....\n")
sleep(1.5)

while chute_usuario != numero_sorteado:

    chute_usuario = int(input("Voce errou! Tente novamente: "))
    print("PROCESSANDO....")
    tentativas += 1
    #Esse comando faz o computador adormecer por um tempo.
    sleep(1.5)

if chute_usuario == numero_sorteado:
        print("Parabéns você acertou!! Voce precisou de {} tentativas".format(tentativas))