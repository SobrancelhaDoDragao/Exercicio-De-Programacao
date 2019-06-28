# -*- coding: utf-8 -*-
# Mostrando o tipo do valor recebido                          -----
#------------------------------------------------------------------
#------------------------------------------------------------------
# Indepedente do que for digitado o valor será um string
# Por isso é necessário formatar o valor com o int
valor = input("Digite um valor: ")
print (type(valor))
#Convertendo para float
valor1 = float(input("Digite um valor: "))
print("Esse é o valor: {} convertido para float".format(valor1))
#Convertendo para boleano
valor2 = bool(input("Digite um valor :"))
print("Esse é: {} o valor convertido para boleano".format(valor2))
