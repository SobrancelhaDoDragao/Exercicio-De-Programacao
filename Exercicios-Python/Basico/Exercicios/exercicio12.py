
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco_bruto = float(input("Digite o preço do produto? "))
desconto = 0.05
preco_a_pagar = preco_bruto - desconto * preco_bruto
print("O preço do produto com desconto é {:.2f}".format(preco_a_pagar))
