filme = {'Titulo': 'Star Wars',
         'Ano': 1977,
         'Diretor': 'George Lucas'
         }
print()
# Métodos do dicionário
print(filme.values())
print(filme.keys())
print(filme.items())

# Mostrando apenas uma valor
print(filme['Titulo'])

# For com dicionarios
for k,v in filme.items():
    print(f'O {k} é {v}')

# Dicionário dentro de uma lista
print()
brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
