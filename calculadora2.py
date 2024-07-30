def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def divisao(a,b):
    if b == 0:
        print('Error: Divisão por zero')
    else:
        return a / b 

def multiplicacao(a,b):
    return a * b

def menu():
    print("Menu:\n"
            "1 - Somar\n"
            "2 - Subtração\n"
            "3 - Divisão\n"
            "4 - Multiplicação\n"
            "5 - Sair\n")

def operacao():
    while True: 
        menu()
        valor_escolhido = input("Escolha uma Operação: ")
        print("___________________________")
        if valor_escolhido == '5':
                print("Saindo do programa.....")
                break
       
        if valor_escolhido in ['1','2','3','4']:
                valor1 = int(input("Primeiro valor: "))
                valor2 = int(input("Segundo valor: "))
        if valor_escolhido == '1':
            print(f" {valor1} + {valor2} = {soma(valor1, valor2)}")
        elif valor_escolhido == '2':
             print(f" {valor1} - {valor2} = {subtracao(valor1, valor2)}")            
        elif valor_escolhido == '3':
            print(f"{valor1} / {valor2} = {divisao(valor1,valor2)}")
        elif valor_escolhido == '4':
             print(f"{valor1} * {valor2} = {multiplicacao(valor1,valor2)}")
        else:
             print("Tente novamente")
if __name__ == "__main__":
     operacao()