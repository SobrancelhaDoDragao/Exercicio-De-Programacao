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
    

def dobro(valor = 0,format = True):
    """
    Essa função retorna o dobro do valor
    """
    if format:
        return formatacao(valor * 2)
    else:
        return valor * 2


def metade(valor = 0,format = True):
    """
    Essa função retorna metade do valor
    """
    if format:
        return formatacao(valor/2)
    else:
        return valor/2


def aumentar(valor = 0,aumento = 0,format = True):
    """
    Essa função recebe dois parâmetros; valor e aumento(Em porcetagem).
    Retorna o valor somado ao aumento
    """
    if format:
        return formatacao(valor +(valor*(aumento/100)))
    else:
        return valor +(valor*(aumento/100))


def diminuir(valor = 0,desconto = 0,format = True):
    """
    Essa função recebe dois parâmetros; valor e desconto(Em porcetagem).
    Retorna o valor com o desconto
    """
    if format:
        return formatacao(valor - (valor*(desconto/100)))
    else:
        return valor - (valor*(desconto/100))


def resumo(valor = 0,aumento = 0,desconto = 0,format = True):
    """
    Essa função retorna todos os dados
    """
    print("-="*30)
    print("Resumo do valor")
    print("-="*30)
    print(f"\nO dobro do preço é {dobro(valor,format = True)}")
    print(f"A metade do preço é {metade(valor,format = True)}")
    print(f"O valor com 10% de aumento é {aumentar(valor,aumento,format = True)}")
    print(f"O valor com 13% de desconto é {diminuir(valor,desconto,format = True)}")
    print("-="*30)