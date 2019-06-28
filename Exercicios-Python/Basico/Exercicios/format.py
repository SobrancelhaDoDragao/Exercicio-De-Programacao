# -*- coding: utf-8 -*-
# No python, se o tipo do valor a ser recebido não for especificado ele considera um string,
# mesmo se for um numero, por isso o "int" antes do input
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
soma = n1 + n2

print("O resultado é {}".format(soma))
