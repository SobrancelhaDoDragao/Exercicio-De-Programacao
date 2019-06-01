# Crie um programa que mostre na tela todos os números pares que 
# estão no intervalo entre 1 e 50
contador = 0
for numeros in range(1,51):
    if int(numeros) % 2 == 0:
        print(numeros)
        contador += 1
print("Dentre todos esses numero existem {} numeros pares".format(contador))
print(contador)