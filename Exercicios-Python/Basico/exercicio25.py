# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input("Digite um nome: ").upper()

if nome.find("SILVA") != -1:
    print("O nome possui silva")
else:
    print("O nome não possui silva")

