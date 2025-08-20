"""
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20%

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_do_produto = "Camiseta"
preco_original = 50.0
porcentagem_de_desconto = (20/100)

desconto = preco_original * porcentagem_de_desconto
preco_total = preco_original - desconto

print(f"O preço original do produto {nome_do_produto} é R${preco_original:.2f}, você obteve um desconto de R${desconto:.2f}, ficando o preço total de R${preco_total:.2f}")