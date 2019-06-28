'''
Crie um programa que leia nome e duas notas de vários alunos e 
guarde tudo em uma lista composta. No final, mostre um boletim 
contendo a média de cada um e permita que o usuário posso mostrar 
as notas de cada aluno individualmente.
'''
temp = []
princ = []
while True:
    nome = str(input('Nome: ')).title().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-'*25)
print(f'N°    NOME                 MÉDIA')
print('_'*35)
for a, n in enumerate(princ):
    print(f'{a}{n[0]:^15}{(n[1] + n[2]) / 2:>15.1f}')
print('_'*35)
while True:
    print('_'*35)
    most = int(input('Mostrar as notas de qual aluno? [999 para interrompe] '))
    if most == 999:
        break
    for a, n in enumerate(princ):
        if most == a:
            print(f'Notas de {n[0]} são [{n[1]},{n[2]}]')
    print('_'*35)
print('_-'*3, '< VOLTE SEMPRE >', '_-'*3)
