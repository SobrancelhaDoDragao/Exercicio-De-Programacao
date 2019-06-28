# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
#-----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Primeiramente o primeiro FOR e executado de acordo do tamanho do array
# "Teste" (no caso 2), depois o segundo FOR executado de acordo com o
# tamanho da palavra infromado, depois e feito a verificação de cada letra
# da palavra usando as variáveis I e J (I para cada palavra e J para cada
# letra)
teste = (
    'Eudson', 'Donateu','Murata','Cachorro'
)
vogais = (
    'A', 'E', 'I', 'O', 'U',
    'a', 'e', 'i', 'o', 'u',
)
for i in range(0, len(teste)):
    print(f"\nNa palavra {teste[i]} temos as vogais: ", end='')
    for t in range(0, len(teste[i])):
        if teste[i][t] in vogais:
            print(f"{teste[i][t]}", end='')
