#-*- coding: utf-8 -*-
# Faça um programa que leia a largura e a altura de uma parede em metros. 
# Calcule a area e a quantidade de tinta para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m quadrados.
print("Digite a altura e a largura da parede em metros:")

altura = float(input("Altura? "))
largura = float(input("Largura? "))

area_parede = altura * largura
tinta_necessaria = area_parede / 2
print("Será necessário {:.2f} litros de tinta, para pintar a parede".format(tinta_necessaria))

