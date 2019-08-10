import os

def Metro(valor,unidade):
    """
    Função que converte valores a partir do metro
    """
    contexto = {'km': 1000,'hm':100,'dam':10,'dm':10,'cm':100,'mm':1000}
    divisao = ('km','hm','dam')

    if unidade in divisao:
        return valor/contexto[unidade]
    else:
        return valor*contexto[unidade]


def Kilometro(valor,unidade):
    """
    Função que converte valores a partir do Kilometro
    """
    contexto = {'hm':10,'dam':100,'m':1000,'dm':10000,'cm':100000,'mm':1000000}

    return valor*contexto[unidade]

def Hectometro(valor,unidade):
    """
    Função que converte valores a partir do Hectometro
    """
    contexto = {'km':10,'dm':10,'m':100,'dm':1000,'cm':10000,'mm':100000}
    divisao = {'km'}

    if unidade in divisao:
        return valor/contexto[unidade]
    else:
        return valor*contexto[unidade]

def Decametro(valor,unidade):
    """
    Função que converte valores a partir do Decametro
    """
    contexto = {'km':100,'hm':10,'m':10,'dm':100,'cm':1000,'mm':10000}
    divisao = ('km','hm')

    if unidade in divisao:
        return valor/contexto[unidade]
    else:
        return valor*contexto[unidade]

def Decimetro(valor,unidade):
    """
    Função que converte valores a partir do Decimetro
    """
    contexto = {'km':10000,'hm':1000,'dam':100,'m':10,'cm':10,'mm':100}
    multiplicacao = ('cm','mm')

    if unidade in multiplicacao:
        return valor*contexto[unidade]
    else:
        return valor/contexto[unidade]


def Centimetro(valor,unidade):
    """
    Função que converte valores a partir do Centimetro
    """
    contexto = {'km':100000,'hm':10000,'dam':1000,'m':100,'dm':10,'mm':10}
    multiplicacao = ('mm')
    
    if unidade in multiplicacao:
        return valor*contexto[unidade]
    else:
        return valor/contexto[unidade]

def Milimetro(valor,unidade):
    """
    Função que converte valores a partir do Milimetro
    """
    contexto = {'km':1000000,'hm':100000,'dam':10000,'m':1000,'dm':100,'cm':10}

    return valor/contexto[unidade]

"""
O programa começa aqui
"""

print("""\n
-------------------------------------------------
Programa para conversão de unidades de medidas
-------------------------------------------------
""")

dadobruto = str(input("\nDigite o valor junto com sua unidade de medida: "))

# Lapidando os dados a partir de uma string
unidade_main = str(dadobruto[-2:]).lower()
valor_main = float(dadobruto[:-2])

# limpando  a tela
os.system('clear')

print("Agora, escolha para qual unidade será convertida? ")

print("""
--------------------------------------------------
                   Unidades
--------------------------------------------------
""",end='')
print("""
 Digite na tela para qual unidade será convertida:
         
       | km | hm | dm | m | dm | cm | mm |
         1     2    3   4    5    6    7
""")
escolha = str(input()).lower()
os.system('clear')

if unidade_main == 'km':
    print(f"O resultado da conversão: {Kilometro(valor_main,escolha)}")

if unidade_main == 'hm':
    print(Hectometro(valor_main,escolha))

if unidade_main == 'dm':
    print(Decametro(valor_main,escolha))

if unidade_main == 'm':
    print(Metro(valor_main,escolha))

if unidade_main == 'dm':
    print(Decimetro(valor_main,escolha))

if unidade_main == 'cm':
    print(Centimetro(valor_main,escolha))

if unidade_main == 'mm':
    print(Milimetro(valor_main,escolha))