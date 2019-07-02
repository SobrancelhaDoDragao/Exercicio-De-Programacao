"""
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite,sacar,depositar e consultar saldo
"""
from historico import Historico
from cliente import Cliente

class Conta():
 
    # Métodos
    def __init__(self,cliente,saldo,limite):
        # Aqui eu passei uma objeto 'cliente' como refêrencia
        # Através dele posso acessar todos os métodos do objeto
        # Assim está classe foi associada a classe cliente
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        print("\nConta criada com sucesso")

    
    def sacar(self,quantia):
        """
        Método para sacar valor da conta
        """
        if quantia > self.saldo:
            print("Não existe saldo sulficiente para esse saque")
            return False
        else:
            self.saldo -= quantia
            return True
            
    
    def depositar(self,deposito):
        """
        Método para depositar valor na conta
        """
        if self.saldo + deposito > self.limite:
            print("O depósito excede o limite da conta, depósito bloqueado!")
            return False
        else:
            self.saldo += deposito
            return True

    def extrato(self):
        """
        Método para mostrar o saldo da conta
        """
        print(f"Seu saldo atual é {self.saldo}")
    
    # O parâmetro self serve para mostrar ao interpretador, que o método pertece a 
    # está classe
    def trasacoes(self,valor,destino):
        """
        Método para realizar um transação
        """
        if self.sacar(valor):
            if destino.depositar(valor):
                self.historico.trasacoes.append(f"Transação de {self.cliente.nome}, para {destino.cliente.nome} no valor de {valor} reais")
                print("Transação efetuada com sucesso")
