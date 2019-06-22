'''
Crie um programa que leia nome, ano de nascimento e carteira de 
trabalho e cadastre-os(com idade) em um dicionário se por acaso a 
CTPS for diferente do ZERO, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
ano_atual = date.today().year
dados = {}

dados['Nome'] = str(input("\nDigite seu nome? "))
dados['Nascimento'] = int(input("Qual ano você nasceu? "))
dados['Carteira de trabalho'] = int(input("Numero da carteira de trabalho?(0 para caso ainda não tenha)"))
dados['Idade'] = ano_atual - dados['Nascimento'] 

if dados['Carteira de trabalho'] != 0:
    dados['Ano de Contratacao'] = int(input("Qual ano você foi contratado? "))
    dados['Salario'] = float(input("Qual é o seu salário? "))
    dados['Aposentadoria'] = dados['Ano de Contratacao'] + 35
    print(f"\nSeu nome é {dados['Nome']}")
    print(f"Sua idade é {dados['Idade']}")
    print(f"Seu salário é {dados['Salario']}")
    print(f"E você irá se aposentar em {dados['Aposentadoria']}")
else:
    dados['Carteira de trabalho'] = 'Não possui'
    print(f"\nSeu nome é {dados['Nome']}")
    print(f"Sua idade é {dados['Idade']}")
    print(f"E não possui carteira de trabalho")

