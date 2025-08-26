"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre
dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações
abaixo:

1 - A calculadora deve solicitar ao usuário que insira dois números e uma operação.
2 - As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
3 - O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
4 - Trate os seguintes erros:
    4.1 - Entrada inválida (não numérica) para os números
    4.2 - Divisão por zero
    4.3 - Operação inválida
5 - Use try/except para capturar e tratar os erros apropriadamente.
6 - Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
7 - Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            print("Erro: Operação inválida. Use +, -, * ou /.")
        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        break
    except ValueError:
        print("Erro: Insira apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")