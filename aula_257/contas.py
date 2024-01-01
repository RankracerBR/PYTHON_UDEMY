import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractclassmethod
    def sacar(self, valor):...

    def depositar(self, valor):
        self.valor += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é: {self.saldo:.2f} ({msg})')
