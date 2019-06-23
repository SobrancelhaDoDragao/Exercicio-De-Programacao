'''
Faça um programa que tenha uma função chamada contador(), que 
receba três parâmetros: início,fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função 
criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada
'''
from time import sleep


def contador(inicio, fim, passo):
    '''
    Essa função conta de acordo com os parâmetros passados
    '''
    if passo == 0:
        passo = 1
        
    print("\nContagem de 1 até 10, de 1 em 1")
    for i in range(1, 11):
        print(f'{i} ', end='')
        sleep(0.5)

    print("\n\nContagem de 10 até 0, de 2 em 2")
    for i in range(10, -1, -2):
        print(f"{i} ", end='')
        sleep(0.5)

    print(f"\n\nContagem de {inicio} até {fim}, de {passo} em {passo}")
    for i in range(inicio, fim, passo):
        print(f"{i} ", end='')
        sleep(0.5)


inicio = int(input("\nInicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)
