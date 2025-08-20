"""
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

Nota 1: 7.5
Nota 2: 8.0
Nota 3: 6.5 

O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

notas = []
for i in range(3):
    while True:
        try:
            nota = float(input(f"Digite a {i + 1}ª nota: "))
            if nota > 10:
                print("A nota não pode ser maior que 10. Tente novamente.")
            elif nota >= 0:
                notas.append(nota)
                break
            else:
                print("A nota não pode ser negativa. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
soma_notas = sum(notas)
media = soma_notas / len(notas)
if media >= 7:
    situacao = "APROVADO!"
else:
    situacao = "REPROVADO!"
print("\n-- RESULTADO --")
for i, nota in enumerate(notas):
    print(f"Nota {i + 1}: {nota:.2f}")
print(f"\nSua média foi de {media:.2f}")
print(f"Você está {situacao}")