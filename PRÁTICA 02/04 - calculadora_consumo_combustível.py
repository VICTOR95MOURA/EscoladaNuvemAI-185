"""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

distancia_Km = 300
gosolina_gasta_L = 25
consumo = distancia_Km / gosolina_gasta_L

print(f"Foram percorridos {distancia_Km} Km, gastos {gosolina_gasta_L} L de gasolina, com um consumo médio de {consumo:.2f} Km/L")