
class Conta_Bancaria: 
    def __init__ (self,titular,saldo_inicial=0):
        self.titular = titular 
        self.saldo = saldo_inicial
       

    def sacar(self, valor):
        if valor > self.saldo:
           print("Saldo insuficiente")
        else:
            self.saldo -= valor 

    def depositar (self,valor):
        self.saldo += valor
    
    def ver_saldo(self):
        print(f"Saldo: R${self.saldo}")
usuario = Conta_Bancaria ("Ismael")

conta = Conta_Bancaria(1000)
conta.ver_saldo()
conta.sacar(200)
conta.depositar(500)


  
















