# Crie uma tupla preenchida com os 20 primeiros colocados da Tabbela do
# Campeonato Brasileiro de Futebol, na ordem de colacação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

tabela = ('Palmeiras', 'Atlético', 'Santos', 'Flamengo', 'Internacional',
          'Bahia', 'Botafogo', 'São Paulo', 'Corinthians',
          'Athletico-PR', 'Ceará SC', 'Goiás', 'Chapecoense', 'Fortazela',
          'Cruzeiro', 'Fluminense', 'CSA', 'Grêmio',
          'Avaí', 'Vasco da Gama')

print(f"\nOs primeiro 5 colocados são {tabela[0:5]}")
print(f"\nOs Ultimos 4 colocados são {tabela[-4:]}")
print("\nOs time em ordem Alfabetica:")
print(f"O Chapecoense está na posição {tabela.index('Chapecoense')+1}")
