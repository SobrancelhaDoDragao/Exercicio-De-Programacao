# Crie um programa que leia dois valores e mostre um menu na tela:

# [1]somar
# [2]Multiplicar
# [3]Maior
# [4]Novos Números
# [5]Sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso
print("Digite dois numero: ")

numero1 = int(input("1º: "))
numero2 = int(input("2º: "))
escolha = 0

print("Qual operação deseja realizar com esses numeros?")

while escolha != 5:
    print("""
    [1]Somar
    [2]Multiplicar
    [3]Novos Números
    [4]Maior
    [5]Sair Do programa\n""")

    escolha = int(input("Digite sua escolha? \n"))

    if escolha == 1:
        soma = numero1 + numero2
        print("-------------------------------------")
        print("Você escolheu Soma\n")
        print("-------------------------------------")
        print("A soma entre {} e {} é {}".format(numero1,numero2,soma))
        print("-------------------------------------")
    if escolha == 2:
        multiplicacao = numero1 * numero2
        print("-------------------------------------")
        print("Você escoheu Multiplicação\n")
        print("-------------------------------------")
        print("A Multiplicação entre {} e {} é {}".format(numero1,numero2,multiplicacao))
        print("-------------------------------------")
    if escolha == 3:
        print("Digite novos numeros: ")
        numero1 = int(input("1º: "))
        numero2 = int(input("2º: "))
    if escolha == 4:
        if numero1 > numero2:
            print("-------------------------------------")
            print("O numero {} é maior que o {}".format(numero1,numero2))
            print("-------------------------------------")
        else:
            print("-------------------------------------")
            print("O numero {} é maior que o {}".format(numero2,numero1))
            print("-------------------------------------")