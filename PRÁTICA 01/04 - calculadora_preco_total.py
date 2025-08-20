produto = {
    "nome do produto": "Cadeira Infantil",
    "preco unitario": 12.40,
    "quantidade": 3
}
print(f"DESCRIÇÃO | QUANTIDADE X VALOR UND. (R$) | VALOR TOTAL (R$)\n{produto["nome do produto"]} | {produto["quantidade"]} X {produto["preco unitario"]:.2f} | {(produto["quantidade"]*produto["preco unitario"]):.2f}")