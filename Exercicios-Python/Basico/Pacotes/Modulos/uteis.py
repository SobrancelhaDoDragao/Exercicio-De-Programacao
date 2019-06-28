"""
Bibliotecas criada para aprender módulos
"""
def fatorial(n):
    """
    Função que recebe um valor como parâmetro, e retorna o fatorial desse valor
    """
    f = 1
    for c in range(1,n+1):
        f*=c
    return f


def dobro(n):
    """
    Retorna o dobro do valor passado por parâmetro
    """
    return n * 2


def triplo(n):
    """
    Retorna o triplo do valor passado por parâmetro
    """
    return n * 3
