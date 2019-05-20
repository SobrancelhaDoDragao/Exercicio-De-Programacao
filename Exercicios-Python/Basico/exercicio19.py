# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele. Lendo o nome deles e escrevendo o nome escolhido.
from random import choice
print("Sorteio dos alunos")
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno : ")
aleatorio = choice([aluno1, aluno2, aluno3, aluno4])
print("O aluno sorteado foi: {}".format(aleatorio))