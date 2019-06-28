# Faça um programa que leia o sexo de uma pessoa, mas só aceite os 
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente 
# até ter um valor correto.
sexo = input("Qual é seu sexo? Apenas 'M' ou 'F' são aceitos como respostas ").upper()

while sexo != 'M' and sexo != 'F':
    sexo = input("Sexo inválido, digite novamente: ").upper()

if sexo == 'M':
    sexo = 'Masculino'

if sexo == 'F':
    sexo = 'Feminino'

print("Seu sexo é",sexo)
