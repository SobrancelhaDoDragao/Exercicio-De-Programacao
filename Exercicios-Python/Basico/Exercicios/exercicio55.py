# Faça um programa que leia o peso de cinco pessoas. No final, 
# mostre qual foi  o maio e o menor peso lidos.
pesos = [float(input('Informe o peso da pessoa {}: '.format(c+1))) for c in range(5)]

print('Maior peso: {}'.format(max(pesos)))
print('Menor peso: {}'.format(min(pesos)))

exit()