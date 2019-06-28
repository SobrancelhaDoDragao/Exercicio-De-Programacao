import uteis

num = int(input("\nDigite um valor: "))
fat = uteis.fatorial(num)

print(f"\nO Fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {uteis.dobro(num)}")
print(f"O triplo de {num} é {uteis.triplo(num)}")