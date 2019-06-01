# Crie um programa que leia uma frase qualquer e diga se ela é um 
# palídromo, desconsiderando os espaços

# EX: 
# Após a sopa
# A sacada da casa
# A torre da derrota
# O lobo ama o bolo
# Anotaram a data da maratona

frase = str(input("Digite uma frase: "))
inverso = frase[::-1]

if frase == inverso:
    print("A frase '{}' é exatamente igual ao seu inverso: '{}'".format(frase,inverso))
    print("Portando é um polídromo")
else:
    print("A frase '{}' não é um polídromo".format(frase))
    
