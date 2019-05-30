# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida

# Média abaixo de 5.0:
# REPROVADO

# Média entre 5.0 e 6.9:
# RECUPERACAO

# Média 7.0 ou superior:
# APROVADO

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2)/2

if media >= 7.0:
    print("APROVADO com a média: {}".format(media))
elif media >= 5.0 and media <= 6.9:
    print("RECUPERACAO média: {}".format(media))
else:
    print("REPROVADO média: {}".format(media))