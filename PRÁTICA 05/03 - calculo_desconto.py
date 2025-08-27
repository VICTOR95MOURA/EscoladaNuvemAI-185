"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após
a aplicação do desconto. Requisitos:

Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.

Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o
percentual de desconto (exemplo: 10).
"""
preco_original = float(input("Qual o valor do produto? "))
porcentagem_desconto = float(input("Qual a porcentagem do desconto? "))
def calculo_desconto(preco_original, porcentagem_desconto):
    desconto = preco_original * (porcentagem_desconto / 100)
    preco_desconto = preco_original - desconto
    return print(f"Com o desconto o preço do produto ficará: R${preco_desconto:.2f}")
calculo_desconto(preco_original, porcentagem_desconto)