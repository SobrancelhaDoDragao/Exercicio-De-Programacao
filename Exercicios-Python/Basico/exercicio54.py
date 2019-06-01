# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atigiram a maioridade e 
# quantas já são maiores

contadormaior = 0
contadormenor = 0

for i in range(1,8):

    idades = int(input("Digite as idades: "))
    if idades >= 18:
        contadormaior += 1
    else:
        contadormenor += 1
print("Dentre todas essa pessoas {} são maiores e {} são menores".format(contadormaior,contadormenor))