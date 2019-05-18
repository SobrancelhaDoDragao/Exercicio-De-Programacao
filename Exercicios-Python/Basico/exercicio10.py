# -*- coding: utf-8 -*-
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$ 1,00 = R$ 3,27
carteira = float(input("Quanto vc tem na carteira? "))
valor_dolar = float(3.27)
poder_de_compra = carteira / valor_dolar
print("Você pode comprar com {} reais, {} Dólares.".format(carteira,poder_de_compra))
