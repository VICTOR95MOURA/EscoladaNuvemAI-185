"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests
def consultar_cep(cep):
    cep = cep.replace("-", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Informe um CEP com 8 dígitos.")
        return
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")
    else:
        print("Erro ao consultar a API.")
if __name__ == "__main__":
    cep = input("Informe o CEP (somente números): ")
    consultar_cep(cep)