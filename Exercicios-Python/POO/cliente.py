"""
EXERCICIO: Crie um software de gerenciamento bancário
Esse softaware poderá ser capaz de criar clientes e contas

Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite,sacar,depositar e consultar saldo
"""


class Cliente():
    """
    Classe cliente, ela possui os atributo e métodos fundamentais de um cliente
    """
    # Atributos
    nome = ''
    idade = 0
    cpf = 0

     
    # Métodos
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        print("\nCliente criado com sucesso")
    

    def dados(self):
        """
        método criado para retornar todos os dados em uma tupla
        """
        dados = {'Nome':self.nome,
                'Idade':self.idade,
                'CPF':self.cpf
                }
        return dados


