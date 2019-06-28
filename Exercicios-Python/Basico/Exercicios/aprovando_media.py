nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta e ultima nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
# Não esqueca os dois ponto.
if media >= 7:
    print("Você foi aprovado! sua média foi: {:.2f}".format(media))
else:
    print("Voce foi reprovado! sua média foi: {:.2f}".format(media))
