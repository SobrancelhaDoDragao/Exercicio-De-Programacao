'''
Faça um programa que tenha uma função chamada maior(), que receba 
vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual 
deles é o maior.
'''


def maior(*valores):
    '''
    Retorna o maior numero dos parâmetros
    '''
    maior = 0
    for i in range(0, len(valores)):
        if [i] == 0:
            valores[i] == maior
        if valores[i] > maior:
            maior = valores[i]
    print(f"\nDentre os valores {valores} o maior é {maior}")


maior(2, 3, 5, 6, 10)
