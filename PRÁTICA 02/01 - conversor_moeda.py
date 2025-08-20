"""
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 

O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

reais = 100
dolar = 5.6
euro = 6.6
conversao_dolar = reais / dolar
conversao_euro = reais / euro
print(f"R${reais:.2f} reais é referente a:\nDolar: US${conversao_dolar:.2f}\nEuro: {conversao_euro:.2f}€")