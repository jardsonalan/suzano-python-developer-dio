class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self.__saldo = saldo # Atributo privado
        self.numero_agencia = numero_agencia # Atributo público

    def depositar(self, valor):
        self.__saldo += valor
        return f'Saldo: R${self.__saldo}'

    def sacar(self, valor):
        self.__saldo -= valor
        return f'Saldo: R${self.__saldo}'
    
    def mostrar_saldo(self):
        return self.__saldo

conta = Conta('0001', 100)
print(conta.depositar(50))
# print(conta.__saldo) # Exibe um error
print(conta.numero_agencia)
print(conta.mostrar_saldo())