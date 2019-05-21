#Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome_completo = input("Digite seu nome completo: ").strip()
print("Seu nome com todas as letras maiúsculas:{}".format(nome_completo.upper()))
print("Seu nome com todas as letras minúscilas:{}".format(nome_completo.lower()))
print("Total de letras que seu nome possui:{}".format(len(nome_completo) - nome_completo.count(' ')))
print("Total de letras do seu primeiro nome é: {}".format(nome_completo.find(" ")))
