# Crie um programa onde o usário digite um expressão qualquer que use 
# parênteses. Seu aplicativo deverá analisar se a expressão passada está 
# com os parênteses abertos e fechado na ordem correta.
expressao = input("\nDigite uma expressão matematica: ")

total = expressao.count('(') + expressao.count(')')

if total % 2 == 0:
    print("Os parênteses da expressão está correta")
else:
    print("A expressão está errada")





        

