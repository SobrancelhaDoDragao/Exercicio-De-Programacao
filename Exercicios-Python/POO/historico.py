"""
Classe criada para compor a classe conta
"""
from datetime import datetime


class Historico():

    def __init__(self):
        self.data_abertura = datetime.today()
        self.trasacoes = []


    def mostrarHistorico(self):
        for i in self.trasacoes:
            print(i)   
