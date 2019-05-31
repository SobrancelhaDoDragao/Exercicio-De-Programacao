# No primeiro parâmetro define o valor da variável usada no for
# O segundo define até onde o valor será incrementado
for quantidade in range(1,11):
    print(quantidade)

print(" ")

# Laço decrescente
for quantidade in range(11,0,-1):
    print(quantidade)

print(" ")

# Laço pulando 2 em 2
for quantidade in range(1,10,2):
    print(quantidade)

# Controlando o valor atráves de um input
numero = int(input("Digite um numero: "))
for c in range(1,numero):
    print("Olá!")