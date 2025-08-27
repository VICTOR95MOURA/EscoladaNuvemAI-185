"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
from datetime import date
ano_nascimento = int(input("Em qual ano você nasceu? "))
def dias_de_vida(ano_nascimento):
    ano_atual = date.today().year
    anos_de_vida = ano_atual - ano_nascimento
    dias_de_vida = anos_de_vida * 365
    return print(f"Sua idade é: {dias_de_vida} dias de vida.")
dias_de_vida(ano_nascimento)