# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# O upper() no final, transforma todas as palavras em maisculo, assim evita erros
cidade = input("Digite uma cidade: ").upper()
cidade = cidade.strip()
# Criando uma lista com o nome da cidade

# Procurando no no indice o nome SANTO

if cidade.find("SANTO") == 0:
    print("O primeiro nome é SANTO")
else:
    print("O primeiro nome não tem SANTO")
