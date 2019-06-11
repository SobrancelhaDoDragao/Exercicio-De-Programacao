# Faça um programa que leia 5 valoes numéricos e guarde-os em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as sua
# respectivas posições na lista.
numeros = []
for i in range(0, 5):
    numeros.append(input(f"Digite o {i+1}º numero: "))

print(
    f"O maior numero é {max(numeros)} sua pocisão é {numeros.index(max(numeros))}")
print(
    f"O menor numero é {min(numeros)} sua pocisão é {numeros.index(min(numeros))}")
