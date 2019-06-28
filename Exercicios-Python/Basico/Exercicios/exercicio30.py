# Crie um programa que leia um número inteiro e mostre na tela se ele 
# é PAR ou IMPAR.

numero = int(input("Digite um numero e eu direi se ele é par ou impar: "))
if numero % 2 == 0:
    print("Ele é par!")
else:
    print("Ele é impar!")