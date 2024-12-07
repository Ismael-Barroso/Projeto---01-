class Carro:
        def __init__(self, cor, modelo, ano , marca):
                self.cor = cor 
                self.modelo = modelo 
                self.ano = ano 
                self.marca = marca 
                self.capacidade = 50 
                self.ligado = False
                self.tanque = 0
        
        def ligar (self):
            self.ligado = True 
        
        def abastecer(self, qtd):
            if(self.tanque +qtd <= self.capacidade):
                  self.tanque += qtd
            else:
                  print('não foi possivel abastecer')
                      
                     


meu_carro = Carro("Preto", "SupraMK4", 2018, "Fiat")
print(meu_carro.marca)

meu_carro.ligar()
print(meu_carro.ligado)

print(meu_carro.tanque)
meu_carro.abastecer(25)
print(meu_carro.tanque)
meu_carro.abastecer(30)
               

        