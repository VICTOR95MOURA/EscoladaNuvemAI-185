"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a
informar a quantidade de caracteres dessa senha aleatória.
"""

import random
import string
def gerar_senha(tamanho):
    if tamanho < 4:
        print("Recomenda-se uma senha com pelo menos 4 caracteres.")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
if __name__ == "__main__":
    try:
        tamanho = int(input("Informe a quantidade de caracteres da senha: "))
        senha = gerar_senha(tamanho)
        print("Senha gerada:", senha)
    except ValueError:
        print("Por favor, informe um número inteiro válido.")