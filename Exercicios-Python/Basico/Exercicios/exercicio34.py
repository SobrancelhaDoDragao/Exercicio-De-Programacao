# Escreva um programa que pergunte o salario de um funcionário de um
# funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1.250, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento de 15%.

salario = float(input("Digite seu salário: "))

if salario > 1250:
       aumento = 0.10
       salario = salario + (salario * aumento)
       print("O salario com aumento é {} reais".format(salario))
if salario<=1250:
       aumento = 0.15
       salario = salario + (salario * aumento)
       print("O salario com aumento é {} reais".format(salario))


