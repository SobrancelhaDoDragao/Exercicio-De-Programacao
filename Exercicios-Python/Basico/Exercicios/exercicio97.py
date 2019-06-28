'''
Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem com
tamanho adaptável.

Ex:
escreva('Olá, Mundo!')

~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
'''


def escreva(texto):
    print('~'*(len(texto) + 2))
    print(f"{texto}")
    print('~'*(len(texto) + 2))

texto='Vou passar'
escreva(texto)
