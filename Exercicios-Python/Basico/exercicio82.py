# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente.

# Ao final, mostre o contéudo das três listas geradas.
mae = []
par = []
impar = []

while True:
    num = int(input("\nDigite um numero: "))
    mae.append(num)

    resposta = input("Deseja continuar? S/N ").upper()

    if resposta == 'N':
        break

for i in range(0,len(mae)):
    if mae[i] % 2 == 0:
        par.append(mae[i])
    else:
        impar.append(mae[i])

print(f"\nPrimeira listas com todos os valores {mae}")
print(f"Segunda lista com todos os valores pare {par}")
print(f"Terceira lista com todos os valores impares {impar}")



