# Faça um programa que leia números e mostre qual é o maior e qual é o menor

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1>num2:
   if num1>num3:
       print("O numero {} é o maior numero".format(num1))
       if num2>num3:
           print("O numero {} é o menor numero".format(num3))
       if num3>num2:
           print("O numero {} é o menor numero".format(num2))
       elif num3 == num2:
           print("Os numero {} e {} são iguais".format(num2,num3))
if num2>num3:
    if num2>num1:
        print("O numero {} é o maior numero".format(num2))
        if num1>num3:
            print("O numero {} é menor numero".format(num3))
        if num3>num1:
            print("O numero {} é o menor numero".format(num1))
        elif num1 == num3:
            print("Os numero {} e {} são iguais".format(num1,num3))
if num3>num1:
    if num3>num2:
        print("O numero {} é o maior numero".format(num3))
        if num2>num1:
            print("O numero {} é o menor numero".format(num1))
        if num1>num2:
            print("O numero {} é o menor numero".format(num2))
        elif num2 == num1:
            print("Os numero {} e {} são iguais".format(num2,num1))

