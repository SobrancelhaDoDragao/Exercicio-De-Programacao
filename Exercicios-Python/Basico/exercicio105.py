"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar 
um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situção (opcional)
"""


def notas(*notas, sit=False):
    """
    Função que recebe um conjunto de notas e calcula a média e também mostrar a maior e a menor nota.
    """
    dicionario = {}
    dicionario['Maior'] = max(notas)
    dicionario['Menor'] = min(notas)
    soma = 0
    
    for i in range(0,len(notas)):
        soma += notas[i]

    dicionario['Media'] = soma/len(notas)
    
    if sit:
        if dicionario['Media'] == 10:
             dicionario['Situacao'] = 'Excelente'
        if dicionario['Media'] >= 7:
            dicionario['Situacao'] = 'Bom'
        if dicionario['Media'] >= 5 and dicionario['Media'] <= 6:
            dicionario['Situacao'] = 'Razoavel'
        if dicionario['Media'] < 5:
            dicionario['Situacao'] = 'Ruim'
    return dicionario


print(notas(4,6,2.5,sit=True))