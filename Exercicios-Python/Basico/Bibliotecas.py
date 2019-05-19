# -*- coding: utf-8 -*-
# Apredendo a importar e usar comandos de bibliotecas(ou Módulos)
# Aqui estou importando todos as funções da biblioteca
# Quando comandos são importados isoladamente, não é necessário botar math.
from math import sqrt,floor
#import math
num = int(input("Digite um numero: "))
raiz = sqrt(num)
print("A Raiz do {}, é {}".format(num,floor(raiz)))
