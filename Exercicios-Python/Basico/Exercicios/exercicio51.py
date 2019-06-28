# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão

quantidade_termos = 10
razao = int(input("Digite a razão da PA: "))

# a variável termos representa a posição do numero da PA desejada
for termos in range(1, quantidade_termos + 1):
    formula = razao + (termos - 1)*razao
    print(formula)
    
