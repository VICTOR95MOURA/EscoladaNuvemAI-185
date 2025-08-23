"""
Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos)
Idoso (60 anos ou mais).
"""
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Digite um número inteiro e positivo.")
        elif idade < 13:
            print("Você é criança.")
            break
        elif idade < 18:
            print("Você é adolescente.")
            break
        elif idade < 60:
            print("Você é adulto.")
            break
        elif idade >= 60:
            print("Você é idoso.")
        else:
            print("Digite um número inteiro e positivo.")
    except ValueError:
        print("Digite um número inteiro e positivo.")