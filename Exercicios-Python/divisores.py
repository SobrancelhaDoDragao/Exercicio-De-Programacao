try:
    numero = int(input('\nDigite um numero: '))
    divisor = []

    for tentativa in range(1,numero + 1):
        if numero % tentativa == 0:
            divisor.append(tentativa)
        
    print(f'\nTodos os divisores de {numero}, são {divisor}')
        
except:
    print("Vc não digitou um numero inteiro\nFim")
