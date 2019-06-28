# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
print('-'*20)
nascimento = int(input('Digite o ano do nascimento: '))
ano_atual = date.today().year

idade = ano_atual - nascimento

if idade <= 9:
    print('O atleta tem {} anos, e sua classificação é JUNIOR!'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, e sua classificação é INFANTIL!'.format(idade))  
elif idade <= 19:
    print('O atleta tem {} anos, e sua classificação é JUNIOR!'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos, e sua classificação é SÊNIOR!'.format(idade))
else:
    print('O atleta tem {} anos, e sua classificação é MASTER!'.format(idade))
 
