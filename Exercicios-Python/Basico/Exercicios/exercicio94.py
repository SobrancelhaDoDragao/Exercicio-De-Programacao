'''
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os 
dicionários em uma lista. No final, mostre:

A)Quantas pessoas foram cadastradas
B)A média de idade do grupo
C)Um lista com todas as mulheres
D)Uma lista com todas as pessoas com idade acima da média.
'''
# Iniciando todas as variáveis

bancoDedados = []
pessoa = {}
totalCadastrados = 0
mediaIdade = 0
soma = 0
mulheres = []

while True:
    pessoa['Nome'] = input("\nQual é o nome da pessoa a ser cadastrada? ")
    pessoa['Sexo'] = input("Qual é o sexo? (M/F) ").upper()

    while pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        pessoa['Sexo'] = input("Sexo inválido digite novamente! (M/F) ").upper()

    pessoa['Idade'] = int(input("Qual é a idade? "))
    bancoDedados.append(pessoa.copy())

    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa.copy())

    totalCadastrados += 1
    soma += pessoa['Idade']
    pessoa.clear()

    continuacao = input("\nQuer Continuar? (S/N)").upper()

    while continuacao != 'N' and continuacao != 'S':
        continuacao = input("Resposta inválida, digite novamente! ").upper()

    if continuacao == 'N':
        break
mediaIdade = soma/totalCadastrados

print(f'\nO total de cadastrados foram {totalCadastrados} e a media da idade deles é {mediaIdade:.2f}')

# Forma de saber se um valor esta vazio no python
if not mulheres:
    print("Nenhuma mulher cadastrada no sistema")
else:
    print(f"\nAs mulheres cadastradas no sistema foram: ")
    for nomes in mulheres:
        print(nomes['Nome'])

