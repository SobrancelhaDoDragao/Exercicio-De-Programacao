# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e codição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista na cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input("Digite preço do produto: "))

print(" ")

print("Digite 1 para: À vista dinheiro/cheque: 10% de desconto")
print("Digite 2 para: À vista na cartão: 5% de desconto")
print("Digite 3 para: Em até 2x no cartão: preço normal")
print("Digite 4 para: 3x ou mais no cartão: 20% de juros")

print(" ")

escolha = int(input("Digite o valor correspodente a escolha:"))
print(" ")

if escolha == 1:
    preco = preco - (preco * 0.10)
    print("O valor a ser pago será de {} reais".format(preco))
if escolha == 2:
    preco = preco - (preco * 0.05)
    print("O valor a ser pago será de {} reais".format(preco))
if escolha == 3:
    # Preço normal
    print("O valor a ser pago será de {} reais".format(preco))
if escolha == 4:
    preco = preco + (preco * 0.20)
    print("O valor a ser pago será de {} reais".format(preco))
    