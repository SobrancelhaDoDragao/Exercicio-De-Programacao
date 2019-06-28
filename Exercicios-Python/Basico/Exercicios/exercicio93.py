'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante 
o campeonato.
'''
desempenho = {}
gols = []

desempenho['Nome'] = str(input("\nDigite seu nome: "))
desempenho['Partidas'] = int(input("\nQuantas partidas foram jogadas? "))
total_de_gols = 0

print(" ")
for t in range(0, desempenho['Partidas']):
    t = int(input(f"Quantos gols na primeira {t + 1}º partida: "))
    gols.append(t)
    total_de_gols += t

print(" ")
desempenho['gols'] = gols[:]
desempenho['Total_De_Gols'] = total_de_gols

print(
    f"O jogador {desempenho['Nome']} jogou {desempenho['Partidas']} partidas")
print(" ")

for i in range(0, desempenho['Partidas']):
    print(f"Na {i+1}º partida o jogador fez {desempenho['gols'][i]} gols")
