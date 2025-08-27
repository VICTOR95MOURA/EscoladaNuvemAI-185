"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e
pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
texto = input("Digite a palavra ou frase a ser verificada: ")
def verificador_palindromo(texto):
    texto_sem_espaco = ''.join(filter(str.isalnum, texto)).lower()
    texo_invertido = texto_sem_espaco[::-1]
    if texto_sem_espaco == texo_invertido:
        return print("É um palíndromo")
    else:
        return print("Não é um palíndromo")
verificador_palindromo(texto)