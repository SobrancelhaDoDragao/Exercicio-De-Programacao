'''
Faça um programa que leia nome e média de um aluno, guardando 
também a situação em um dicionário. No final, mostre o conteúdo 
da estrutura na tela.
'''
usuario = {}
usuario['Nome'] = input("\nQual é seu nome? ")
usuario['Media'] = float(input("Qual é sua média? "))
print(f"Seu nome é {usuario['Nome']} e sua média é {usuario['Media']}")
if usuario['Media'] >= 7:
    print("Aprovado!")
print("Reprovado!")
# print(usuario)
