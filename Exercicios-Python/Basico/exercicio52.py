# Faça um programa que leia um número inteiro e diga se é ou não um
# número primo

numero = int(input("Digite um numero: "))
contador = 0

print(" ")

# Testando os divisores
for divisor in range(1, numero + 10):
    if numero % divisor == 0:
        contador += 1
        print("Divisores de {} são: {}\n".format(numero, divisor))

# Caso encotre apenas dois divisores o numero é primo
if contador == 2:
    print("O numero {} é primo".format(numero))
else:
    print("O numero {} não é primo".format(numero))
