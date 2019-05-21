# Faça um programa que leia um frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece na primeira vez.
# Em que posiçao ela aparece na ultima vez.

frase = input("Digite a uma frase: ").upper()
print("A letra 'A' aparece {} vezes, na primeira vez ela aparece na posição {}, e na ultima vez na posição {}".format(frase.count('A'),frase.find('A')+1,frase.rfind('A')+1))