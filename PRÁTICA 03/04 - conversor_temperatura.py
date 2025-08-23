"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
while True:
    unidade_medida = input("Qual a unidade de medida da temperatura (Celsius, Fahrenheit ou Kelvin)? ").upper()
    if unidade_medida == "CELSIUS":
        temperatura = float(input("Digite o valor da temperatura em Celsius (°C): "))
        fahrenheit = (temperatura * 9 / 5) + 32
        kelvin = temperatura + 273.15
        print(f"{temperatura:.2f}°C corrensponde a {fahrenheit:.2f}°F ou {kelvin:.2f} K")
        break
    elif unidade_medida == "FAHRENHEIT":
        temperatura = float(input("Digite o valor da temperatura em Fahrenheit (°F): "))
        celsius = (temperatura - 32) * 5 / 9
        kelvin = ((temperatura - 32) * 5 / 9) + 273.15
        print(f"{temperatura:.2f}°F corrensponde a {celsius:.2f}°C ou {kelvin:.2f} K")
        break
    elif unidade_medida == "KELVIN":
        temperatura = float(input("Digite o valor da temperatura em Kelvin (K): "))
        celsius = temperatura - 273.15
        fahrenheit = ((temperatura - 273.15) * 9 / 5) + 32
        print(f"{temperatura:.2f} K corrensponde a {celsius:.2f}°C ou {fahrenheit:.2f}°F")
        break
    else:
        print("Digite uma das três opções: Celsius, Fahrenheit ou Kelvin!")
        print(unidade_medida)
