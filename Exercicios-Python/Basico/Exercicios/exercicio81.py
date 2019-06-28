# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

# A)Quantos números foram digitados.
# B)A lista de valores, ordenada de forma decrescente.
# C)Se o valor 5 foi digitado e está ou não nam lista.

lista = []

cont = 0

while True:

    num = int(input("\nDigite o numero: "))
    lista.append(num)

    reposta = input("Deseja continuar? S/N ").upper()

    if reposta == 'N':
        break

lista.sort(reverse=True)

print(f"\nO valore foram: {lista}")
print(f"Foram digitados {len(lista)} numeros")
if 5 in lista:
    print(
        f"O numero 5 existe na lista e ele se encontra na posição {lista.index(5)}")
else:
    print("O valor 5 não existe na lista")
