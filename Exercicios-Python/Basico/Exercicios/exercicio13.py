# -*- coding: utf-8 -*-
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Digite seu salário: "))
aumento = 0.15
salario_com_aumento = salario + aumento * salario
print("O salário com aumento é {}".format(salario_com_aumento))
