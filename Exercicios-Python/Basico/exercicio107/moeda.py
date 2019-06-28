"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
diminuir(),dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

def dobro(valor):
    """
    Essa função retorna o dobro do valor
    """
    return valor * 2


def metade(valor):
    """
    Essa função retorna metade do valor
    """
    return valor/2


def aumentar(valor,aumento):
    """
    Essa função recebe dois parâmetros; valor e aumento(Em porcetagem).
    Retorna o valor somado ao aumento
    """
    return valor +(valor*(aumento/100))


def diminuir(valor,desconto):
    """
    Essa função recebe dois parâmetros; valor e desconto(Em porcetagem).
    Retorna o valor com o desconto
    """
    return valor - (valor*(desconto/100))