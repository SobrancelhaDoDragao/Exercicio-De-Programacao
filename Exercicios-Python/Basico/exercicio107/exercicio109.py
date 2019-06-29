"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um 
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado 
pela função moeda(), desenvolvida no exercicio 108.
"""
import moeda


p = float(input("\nDigite o preço: "))

print(f"\nO dobro do preço é {moeda.dobro(p)}")
print(f"A metade do preço é {moeda.metade(p)}")
print(f"O valor com 10% de aumento é {moeda.aumentar(p,10)}")
print(f"O valor com 13% de desconto é {moeda.diminuir(p,13)}")