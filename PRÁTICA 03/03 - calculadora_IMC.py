"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar o peso (em kg) e a
altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""
peso = int(input("Digite seu peso em quilogramas (Kg): "))
altura = float(input("Digite sua altura em metros (m): "))
imc = peso / altura ** 2
if imc < 18.5:
    print(f"Você está abaixo do peso. IMC = {imc:.2f}")
elif imc < 25:
    print(f"Você está com peso normal. IMC = {imc:.2f}")
elif imc < 30:
    print(f"Você está com excesso de peso. IMC = {imc:.2f}")
elif imc < 35:
    print(f"Você está com obesidade classe 1. IMC = {imc:.2f}")
elif imc < 40:
    print(f"Você está com obesidade classe 2. IMC = {imc:.2f}")
else:
    print(f"Você está com obesidade classe 3. IMC = {imc:.2f}")