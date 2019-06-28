'''
Faça um programa que tenha uma lista chamada números e duas 
funções chamadas sorteia() e somaPar().A primeira função vai 
sortear 5 números e vai colocá-los dentro da lista e a segunda 
função vai mostrar a soma entre todos os valores PARES sorteados 
pela função anterior.
'''
from random import randint


def sorteia():
    lista = [randint(0, 10), randint(0, 10), randint(
        0, 10), randint(0, 10), randint(0, 10)]
    print(f"\nOs valores sorteado forão: {lista}")
    return lista


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"A soma dos pares é {soma}")


somaPar(sorteia())
