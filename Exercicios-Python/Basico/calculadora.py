# -*- coding: utf-8 -*-
# Operações no Python
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divicao = numero1/numero2
# O :2.F serve para formatar o valor
print("A soma é:{}, a subtração é {}, a multiplicacão é {}, divisão é {:.2f}".format(soma,subtracao,multiplicacao,divicao))
