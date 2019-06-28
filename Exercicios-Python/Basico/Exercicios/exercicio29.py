# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$7.00 por cada quilometro acima do limte.
from time import sleep
velocidade = float(input("Digite a velocidade do veículo: "))

if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 7
    print("Multado!! Valor da multa {} reais".format(multa))
else:
    print("Veiculo dentro da velocidade permitida")
    
