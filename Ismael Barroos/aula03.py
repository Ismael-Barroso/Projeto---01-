class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def ver_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")

# Exemplo de uso
conta = ContaBancaria(1000)
conta.ver_saldo()
conta.sacar(200)
conta.depositar(500)