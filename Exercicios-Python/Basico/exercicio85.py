"""
Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e 
ímpares em ordem crescente.
"""
todos = []
par = []
impar = []
for t in range(0,8):
    numero = int(input("\nDigite um numero: "))

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
impar.sort()

todos.append(par[:])
todos.append(impar[:])

print(todos)