# Refaça o exercicio 9, mostrando a tabuada de um número que o 
# usuário escolher, só que agora utilizando um laço for.
print("-----------------TABUADA--------------------")
numeroqualquer = int(input("Digite um numero qualquer: "))
print(" ")

for tabuada in range(1,11):
    print("{}*{} = {} ".format(numeroqualquer,tabuada,numeroqualquer*tabuada))
