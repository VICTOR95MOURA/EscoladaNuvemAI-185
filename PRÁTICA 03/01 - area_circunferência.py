"""
A fórmula para calcular a área de uma circunferência é: área = π x raio2. Considerando para este problema que π = 3.14159265: 

• Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal.
"""
pi = 3.14159265
while True:
    entrada = input("Para calcular a área da circuferência você prefere usar o raio ou diametro? ").upper()
    if entrada == "RAIO":
        variavel = float(input("Qual o valor do raio em cm? "))
        area = pi * variavel ** 2
        print(f"A área circular é igual a {area:.2f} cm²")
        break
    elif entrada == "DIAMETRO":
        variavel = float(input("Qual o valor do diametro em cm? "))
        area = pi * (variavel / 2) ** 2
        print(f"A área circular é igual a {area:.2f} cm²")
        break
    else:
        print("Digite uma entrada válida! Digite RAIO ou DIAMETRO!")