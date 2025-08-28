"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
from datetime import date
ano_nascimento = int(input("Em qual ano você nasceu? "))
mes_nascimento = int(input("Em qual mês você nasceu? "))
dia_nascimento = int(input("Em qual dia você nasceu? "))
def dias_de_vida(ano_nascimento):
    ano_atual = date.today().year
    anos_de_vida = ano_atual - ano_nascimento
    bissexto = 0
    for ano in range(ano_nascimento, ano_atual):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            bissexto += 1
        else:
            continue
    mes_dias = (date.today().month - mes_nascimento) * 30
    dias = date.today().day - dia_nascimento
    dias_de_vida = (anos_de_vida * 365) + bissexto + mes_dias + dias
    return print(f"Sua idade é: {dias_de_vida} dias de vida.")
dias_de_vida(ano_nascimento)