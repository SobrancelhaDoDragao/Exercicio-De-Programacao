"""
Aqui todas as classes serão importadas e instânciadas
"""
from cliente import Cliente
from conta import Conta


# Instânciado cliente
Cliente1 = Cliente('Eudson',21,'065.070.241.43')
# Instânciando Conta
Conta1 = Conta(Cliente1,1000,5000)

# Segundo cliente sendo instânciado para realizar a transação
Cliente2 = Cliente('Galileu',30,'053.210.056')
# Segunda conta para o novo cliente
Conta2 = Conta(Cliente2,5000,10000)

# Realizando a transação de valores entre contas
Conta2.trasacoes(2943,Conta1)
Conta2.trasacoes(1000,Conta1)

print(Conta2.historico.mostrarHistorico())
