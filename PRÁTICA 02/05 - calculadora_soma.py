"""
Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 

Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.
"""

lista = []
for i in range(2):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número: "))
            lista.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
soma_numeros = sum(lista)
print(f"A soma do número A = {lista[0]} e B = {lista[1]} é igual a {soma_numeros}")