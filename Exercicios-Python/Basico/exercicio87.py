'''
Aprimore o desafio anterior, mostrando no final:

A)A soma de todos os valores pares digitados.
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda linha
'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
SomarPar = 0
TercColum = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"\nDigite um valor para {l}|{c}: "))
        if c == 2:
            TercColum += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            SomarPar += matriz[l][c]
# For pra exibir os valores na tela           
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]",end = ' ')
    print()

print(f"A soma dos valores pares é {SomarPar}")
print(f"A soma dos valores da terceira coluna é {TercColum}")
print(f"O maior valor da segunda linha {max(matriz[1])}")