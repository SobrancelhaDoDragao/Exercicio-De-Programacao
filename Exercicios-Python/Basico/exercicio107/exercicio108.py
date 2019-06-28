"""
Adapte o código do desafio 107, criando uma função adicional chamada moeda() 
que consiga mostrar os valores como um valor monetário formatado.
"""
import moeda


p = float(input("\nDigite o preço: "))

print(f"\nO dobro do preço é {moeda.formatacao(moeda.dobro(p))}")
print(f"A metade do preço é {moeda.formatacao(moeda.metade(p))}")
print(f"O valor com 10% de aumento é {moeda.formatacao(moeda.aumentar(p,10))}")
print(f"O valor com 13% de desconto é {moeda.formatacao(moeda.diminuir(p,13))}")