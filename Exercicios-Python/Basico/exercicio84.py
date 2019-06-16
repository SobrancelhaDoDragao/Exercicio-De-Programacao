"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em 
uma lista. 
No final, mostre:

A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas
C)Um listagem com as pessoas mais leves
"""
pessoas = []
dados = []
i = 1
menor = maior = 0
while True:
    print(f'\nDados da {i}º pessoa: ')

    # Aqui estou limpando a variável para não inserir dados antigos
    dados.clear()
    dados.append(input("Nome: "))
    dados.append(input("Peso: "))

    # Esse comando ':' adiciona uma cópia dos dados da lista
    # Assim é possível burla o vinculo entre as duas
    pessoas.append(dados[:])

    controle = input("Quer continuar? [S/N]").upper()
    if controle == 'N':
        break
    i += 1

for pocisao in range(0, len(pessoas)):
    if pocisao == 0:
        maior = pessoas[pocisao]
    if pessoas[pocisao][1] > maior[0][1]:
        maior = pessoas[pocisao]

for pocisao in range(0, len(pessoas)):
    if pocisao == 0:
        menor = pessoas[pocisao]
    if pessoas[pocisao][1] < menor[0][1]:
        menor = pessoas[pocisao]
   
print(f"Os mais pesado é: {maior}")
print(f"O mais leve é: {menor}")
print(f"O total de pessoas cadastradas foram {len(pessoas)}")


