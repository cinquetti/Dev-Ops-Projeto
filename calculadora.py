def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possivel dividir por zero"

def calculadora(escolha):
    
    if escolha not in ['1', '2', '3', '4']:
        return ("Escolha inválida!")
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    if num1.isnumeric() and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)
    else: return "Entrada inválida!"

    if escolha == '1':
        return soma(num1, num2)
    elif escolha == '2':
        return subtracao(num1, num2)
    elif escolha == '3':
        return multiplicacao(num1, num2)
    elif escolha == '4':
        return divisao(num1, num2)
    
def run_calculadora():
    print("Selecione o número da operação desejada:")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")
    print(calculadora(escolha))
