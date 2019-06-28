# -*- coding: utf-8 -*-
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, 
# calcule e mostre o comprimento da hipotenusa
from math import sqrt,pow
print("     Calculo de Hipotenusa")
print("-----------------------------------")
a = float(input("Digite a medida do lado triângulo Retangulo: "))
b = float(input("Digite a medida do lado triângulo Retangulo: "))
hipotenusa = pow(a,2) + pow(b,2)
hipotenusa = float(sqrt(hipotenusa))
input("A hipotenusa é {:.2f}".format(hipotenusa))