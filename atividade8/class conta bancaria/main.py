class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"seu saldo agora é: {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"seu saldo agora é: {self.saldo}")
            return True
        else:
            print("Saldo insuficiente.")
            return False
        
        
minhaContaBancaria = ContaBancaria()

minhaContaBancaria.depositar(0)
minhaContaBancaria.sacar(0)