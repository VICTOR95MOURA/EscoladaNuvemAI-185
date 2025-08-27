"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros: 
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 
float: O valor da gorjeta calculada
"""
valor_conta = float(input("Qual o valor total da conta? "))
porcentagem_gorjeta = float(input("Qual a porcentagem da gorjeta? "))
def calculo_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return print(f"O valor da gorjeta é R${gorjeta:.2f}")
calculo_gorjeta(valor_conta, porcentagem_gorjeta)