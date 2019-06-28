# Crie um programa que tenha uma tupla totalmente preencida com uma contagem por extenso, 
# de zero até vinte.

# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
16
numeros = ('Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dizesseis','Dizessete','Dizoito','Dizenove','Vinte')

Num_usuario = int(input('Digite um numero de 1 a 20: '))

while Num_usuario > 20 or Num_usuario < 0:
    Num_usuario = int(input('Numero invalido! Digite novamente: '))

print(f"Você digitou o numero {numeros[Num_usuario-1]}")