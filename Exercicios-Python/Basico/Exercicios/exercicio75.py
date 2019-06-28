# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla no final, mostre:

# A)Quantas vezes apareceu o valor 9.
# B)Em que posição foi digitado o primeiro valor 3.
# C)Quais foram os números pares.

cont = 0
pocisao3 = 5
contPar = 0

valores = (
    int(input("\nDigite o primieiro valor: ")),
    int(input("Digite o segundo valor: ")),
    int(input("Digite o terceiro valor: ")),
    int(input("Digite o quarto valor: "))
)
for i in range(0, 4):
    if valores[i] % 2 == 0:
        contPar += 1
    if valores[i] == 9:
        cont += 1
    if valores[i] == 3:
        if pocisao3 == 5:
            pocisao3 = i

print(
    f"\nOs valores da tuplas são {valores}, e o nove aparece {cont} vezes, e foram encotrados {contPar} numeros pares")

if pocisao3 == 5:
    print("o valor 3 não foi encontrado")
else:
    print(f"o valor 3 foi encontrado na posição {pocisao3}")

# Seria muito mais simples fazer esse exercício se eu usa-se os métodos
# nativos do Python
