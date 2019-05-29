# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma 
# mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

nu1 = int(input("Digite um numero: "))
nu2 = int(input("Digite um numero: ")) 

if nu1>nu2:
    print("O primeiro valor é maior")
elif nu2>nu1:
    print("O segundo valor é maior")
else:
    print("Os dois valores são iguais")
