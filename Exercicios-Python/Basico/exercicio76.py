# Crie um programa que tenha um tupla única com nomes de produtos e
# seus respectivos preços, na sequência.

# No final, mostre uma listagem de preços, organizando os dados em
# forma tabular.

listagem = (
    'Arroz',10.60,'Carne',20.50,'Manteiga',4.60,'Chocolate',7.00,
    'Oleo de soja',22.60
)
print("\n------------------------------------------")
print("           LISTAGEM DE PREÇOS             ")
print("------------------------------------------")
print(f"{listagem[0]}-----------------------------R$  {listagem[1]}")
print(f"{listagem[2]}-----------------------------R$  {listagem[3]}")
print(f"{listagem[4]}---------------------------R$  {listagem[5]}")
print(f"{listagem[6]}--------------------------R$  {listagem[7]}")
print(f"{listagem[8]}----------------------R$  {listagem[9]}")
print("------------------------------------------")
