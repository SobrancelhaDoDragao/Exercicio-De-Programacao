# Desenvolva um programa que leia o comprimento de tr�s retas e diga ao usu�rio se elas podem ou n�o formar um tri�ngulo.

lado1 = float(input("Digite o lado triângulo: "))
lado2 = float(input("Digite o outro do lado triângulo: "))
lado3 = float(input("Digite o ultimo lado do triângulo: "))

if lado1>lado2+lado3:
     print("Essas medidas não formam um triângulo")
if lado2>lado3+lado1:
     print("Essas medidas não formam um triângulo")
if lado3>lado2+lado1:
     print("Essas medidas não formam um triângulo")
else:
     print("Essas medidas formam um triângulo")
