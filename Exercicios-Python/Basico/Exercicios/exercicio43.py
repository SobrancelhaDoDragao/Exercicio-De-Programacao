# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
# IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

from math import pow

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

IMC = peso/pow(altura,2)

# Abaixo de 18.5: Abaixo do peso
if IMC < 18.5:
    print("Abaixo do peso IMC = {:.1f}".format(IMC))
# Entre 18.5 e 25: Peso ideal
elif IMC >= 18.5 and IMC <= 25:
    print("Peso ideal IMC = {:.1f}".format(IMC))
# 25 até 30: Sobrepeso
elif IMC > 25 and IMC <= 30:
    print("Sobrepeso IMC = {:.1f}".format(IMC))
# 30 até 40: Obesidade
elif IMC > 30 and IMC <= 40:
    print("Obesidade IMC = {:.1f}".format(IMC))
# Acima de 40: Obesidade mórbida
elif IMC > 40:
    print("Obesidade mórbida IMC = {:.1f}".format(IMC))
