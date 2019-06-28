"""
Faça um minisistema que utilize o Interactive Help do Python. O usuário vai 
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 
'Fim', o programa se encerrará.

OBS: use cores.
"""
from time import sleep


def ajuda(comando):
    help(comando)


while True:
    comando = input("\nDigite o comando qual deseja saber? ")
    print("Procurando...")
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
