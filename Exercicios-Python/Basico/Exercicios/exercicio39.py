# Faça um programa que leia o ano de nascimento de um jovem e informa, 
# de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
nascimento = int(input("Digite sua data de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - nascimento

if idade == 18:
    print("Está na hora de se alistar!")
elif idade > 18:
    atraso = idade - 18
    print("Você devia ter se alistado a {} anos atrás, vá se alistar agora!!".format(atraso))
else:
    print("Você ainda é menor de idade, não precisa se alistar")