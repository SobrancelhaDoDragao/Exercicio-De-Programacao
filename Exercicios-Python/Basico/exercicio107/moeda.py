"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
diminuir(),dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


def formatacao(valor = 0):
    """
    Formata os valores para o monetário
    """
    return f"R$ {valor:.2f}"
    

def dobro(valor = 0):
    """
    Essa função retorna o dobro do valor
    """
    return valor * 2


def metade(valor = 0):
    """
    Essa função retorna metade do valor
    """
    return valor/2


def aumentar(valor = 0,aumento = 0):
    """
    Essa função recebe dois parâmetros; valor e aumento(Em porcetagem).
    Retorna o valor somado ao aumento
    """
    return valor +(valor*(aumento/100))


def diminuir(valor = 0,desconto = 0):
    """
    Essa função recebe dois parâmetros; valor e desconto(Em porcetagem).
    Retorna o valor com o desconto
    """
    return valor - (valor*(desconto/100))