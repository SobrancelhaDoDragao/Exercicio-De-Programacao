'''
Faça um programa que tenha uma função chamada área(), que receba as 
dimensões de um terreno retangular(largura e comprimento) e mostre a 
área do terreno.
'''
def CalculoArea():
    '''
    Calcula a area do terreno
    '''
    print("\nControle de terrenos")
    print('-='*30)

    comprimento = float(input("Comprimento(m): "))
    largura = float(input("Largura (m): "))

    area = comprimento * largura

    print(f"A área do terreno com {comprimento} metros de comprimenro e {largura} metros de largura é {area}m²")


CalculoArea()