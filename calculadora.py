from flask import Flask, request, render_template

calculadora = Flask(__name__)

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
        return "Não é possível dividir por zero"

@calculadora.route('/')
def index():
    return render_template('index.html')

@calculadora.route('/calcular', methods=['POST'])
def calcular():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']

        if operacao == '1':
            resultado = soma(num1, num2)
        elif operacao == '2':
            resultado = subtracao(num1, num2)
        elif operacao == '3':
            resultado = multiplicacao(num1, num2)
        elif operacao == '4':
            resultado = divisao(num1, num2)
        else:
            resultado = "Escolha inválida!"

    except ValueError:
        resultado = "Entrada inválida!"

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    calculadora.run(debug=True)
