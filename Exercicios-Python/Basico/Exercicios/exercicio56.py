# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

media = 0
max = 0
min = 0
cont = 0
velho = 0
novo = 0
for i in range(1, 5):
    nome = str(input("Digite o nome da {}ª pessoa: ".format(i))
               ).strip().capitalize()
    idade = int(input("Digite a idade do(a) {}: ".format(nome)))
    sexo = str(input("Digite o sexo do(a) {}: ".format(nome))).strip().lower()
    print("")
    media += idade
    if i == 1 and sexo == "m" or sexo == "masculino":
        max = idade
        min = idade
        if idade == max:
            velho = nome
        elif idade == min:
            novo = nome
    elif idade > max:
        max = idade
        velho = nome
    elif idade < min:
        min = idade
        novo = nome
    elif idade < 20 and sexo == "f" or sexo == "feminino":
        cont += 1
print("A média de idade do grupo é {:.2f}".format(media / 4))
print("O homem mais velho tem {} anos e seu nome é {}".format(max, velho))
print("A quantidade de mulheres que tem menos de 20 anos é {}".format(cont))
