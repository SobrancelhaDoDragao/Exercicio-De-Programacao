# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltipla de três e que se encontram no intervalo de
# 1 até 500
contador = 0
for numeros in range(1, 501):
    # Verificando se o numero é impar
    if numeros % 2 != 0:
        # Verificando se é multiplo de 3
        if numeros % 3 == 0:
            contador += numeros
print(" ")
print("A soma de todos os numero ímpares, que são multiplos de 3")
print("e que se encotram no intervalo de 1 a 500 é: {}".format(contador))
