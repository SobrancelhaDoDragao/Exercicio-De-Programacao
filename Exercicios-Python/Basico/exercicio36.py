# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa. O salário do comprador e em quantos anos
# ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa desejada: "))
salario = float(input("Digite seu salário: "))
tempo_extimado = float(input("Em quantos anos você espera quitar a casa? "))

# Conversão de anos para meses
tempo_em_meses = tempo_extimado * 12
mensalidade = valor_casa/tempo_em_meses

if mensalidade > salario * 0.30:
    print("Empréstimo negado, a mensalidade excede 30% do seu salário.")
else:
    print("Sua prestação mensal será de {} reais".format(mensalidade))
