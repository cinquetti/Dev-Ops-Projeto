import requests

def authenticate():
    token = input("Digite o token de autenticação: ")
    response = requests.post('http://auth_service:5006/auth', json={'token': token})
    if response.json()['status'] == "authorized":
        return True
    else:
        return False

def log_operation(operation, a, b, result):
    data = {'operation': operation, 'a': a, 'b': b, 'result': result}
    requests.post('http://log_service:5005/log', json=data)

def calculadora(escolha):
    if escolha not in ['1', '2', '3', '4']:
        return "Escolha inválida!"
    
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    if num1.isnumeric() and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)
    else:
        return "Entrada inválida!"

    data = {'a': num1, 'b': num2}
    operation = ''
    
    if escolha == '1':
        response = requests.post('http://soma_service:5001/soma', json=data)
        operation = 'soma'
    elif escolha == '2':
        response = requests.post('http://subtracao_service:5002/subtracao', json=data)
        operation = 'subtracao'
    elif escolha == '3':
        response = requests.post('http://multiplicacao_service:5003/multiplicacao', json=data)
        operation = 'multiplicacao'
    elif escolha == '4':
        response = requests.post('http://divisao_service:5004/divisao', json=data)
        operation = 'divisao'
    
    result = response.json()['result']
    log_operation(operation, num1, num2, result)
    
    return result

def run_calculadora():
    if not authenticate():
        return "Autenticação falhou!"

    print("Selecione o número da operação desejada:")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")
    print(calculadora(escolha))

if __name__ == '__main__':
    run_calculadora()
