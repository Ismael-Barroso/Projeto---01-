class Calculadora:
    def __init__(self):
        pass


    def somar(self,n1,n2):
        resultado = n1+ n2 
        print(resultado)
    
    def subtrair(self,n1,n2):
        resultado = n1 - n2 
        print(resultado)

    def multiplicar (self,n1,n2):
        resultado = n1 * n2 
        print(resultado)

    def dividir (self,n1,n2):
        resultado = n1 / n2 
        print(resultado)



calcular = Calculadora ()



def menu ():
    print('Digite 1 - para somar')
    print("Digite 2 - para subtrair")
    print("Digite 3 - para multiplicar")
    print("Digite 4 - para dividir")
    valor = (int(input("Digite a opção desejada : ")))
    print(valor)

    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um valor:"))

    if valor == 1:
       resultado_soma =  calcular.somar(n1,n2)
       print(f"A soma de {n1} e {n2} é {resultado_soma}")
    if valor == 2:
        resultado_subtrair = calcular.subtrair(n1,n2)
        print(f"A subtração de {n1} e {n2} é {resultado_subtrair}")
        
    if valor == 3:
        resultaro_multiplicar = calcular.multiplicar(n1,n2)
        print(f"a Multiplicação de {n1} e {n2} é {resultaro_multiplicar}")

    if valor == 4:
        resultado_divisao = calcular.dividir(n1,n2)
        print(f"A divisão de {n1} e {n2} é {resultado_divisao}")

    else:
        print("Digite um valor válido !")

menu()







    