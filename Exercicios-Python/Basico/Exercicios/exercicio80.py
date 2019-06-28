# Crie um programa onde o usuário possa digitar cinco valores numéricos e 
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o 
# sort()).

# No final, mostre a lista ordenada na tela.
numeros = list()

for i in range(0,5):
    n = int(input(f"Digite o {i+1}º valor: "))
    
    if i == 0:
        numeros.append(n)
    elif n > numeros[i-1]:
        numeros.append(n)
    else:
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao,n)
                break
        posicao += 1 
print(numeros)