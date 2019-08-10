try:
    numero = int(input('\nDigite um numero: '))
    divisor = []

    for tentativa in range(1,numero + 1):
        if numero % tentativa == 0:
            divisor.append(tentativa)
            
    if len(divisor) == 2:
        print(f'\nO numero {numero} é primo')

    print(f'\nTodos os divisores do {numero} são: {divisor}')
        
except:
    print("Vc não digitou um numero inteiro\nFim")
