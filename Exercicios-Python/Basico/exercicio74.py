# Crie um programa que vai gerar cinco números aleatótios e colocar em 
# uma tupla.

# Depois disso, mostre a listagem de números gerados e também 
# indique o menor e o maior valor que estão na tupla.
from random import randint

numeros = (randint(0,20),randint(0,20),randint(0,20),
           randint(0,20),randint(0,20))
print(f"\nA lista com numero sorteados: {numeros}, o maior numero é {max(numeros)} e o menor {min(numeros)}")