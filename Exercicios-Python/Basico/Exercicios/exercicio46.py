# Faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de 
# artificio, indo de 10 até 0, com um pausa de 1 segundo entre eles.
from time import sleep
print(" ")

print("Contagem regressiva para estouro dos fogos:")

print(" ")

for contador in range(10,0,-1):
    print("Faltam {} segundos".format(contador))
    sleep(1)  
print("Bummmmm!!!!!!!!")   
