# Desenvolva um programa que leia seis números inteiros e mostre a soma 
# apenas daqueles que forem pares. Se o valor digitado for ímpar, 
# desconsidere-o
soma = 0
contador = 0
for c in range(1,7):
    num = int(input("Digite o {}º numero: ".format(c)))
    if num % 2 == 0:
        contador += 1
        soma += num
print("A soma dos {} numeros pares é {}".format(contador,soma))