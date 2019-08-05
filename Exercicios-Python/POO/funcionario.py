"""
Aprendendo Herança em Python
"""
from cliente import Cliente

# Essa classe Herda métodos é atributos da classse Cliente
class Funcionario(Cliente):
    # Polimorfismo
    # Sobrepondo o init da classe mãe
     def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        print("\nFuncionário criado com sucesso")

f = Funcionario("Rumineu",25,'348074')
print(f.dados())