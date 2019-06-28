# Desenvolva um programa que pergunte a distância de uma viagem em km. 
# Calcule o preço da passagem,cobrando R$0,50 por km para viagens de 
# até 200km e R$0,45 para viagens mais longas.

distancia = float(input("Digite a distancia da viagem: "))

if distancia <= 200:
    taxa = distancia * 0.50
    print("O preço da passagem é {} reais".format(taxa))
else:
    taxa = distancia * 0.45

    print("O preço da passagem é {:.2f} reais".format(taxa))