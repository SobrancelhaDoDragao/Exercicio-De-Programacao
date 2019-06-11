# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não sera adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.
infiteNum = []

while True:
    Num = int(input("\nDigite um valor: "))

    if Num in infiteNum:
        print("Esse numero já existe na lista")
    else:
        infiteNum.append(Num)
        print("Valor Adicionado com sucesso")

    continua = str(input("Quer Continuar S/N \n")).upper()

    if continua == 'N':
        break
# Esse comando ele altera a orden na lista diretamente (como um ponteiro), ele não funciona no
# print
infiteNum.sort()

print(f"Os numeros da lista são {infiteNum}") 
 
