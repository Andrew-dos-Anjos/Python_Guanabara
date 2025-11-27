#Lista de Preços com Tupla
# ----------

print("-"*40)
print(f"{"Tabela de Preços":^40}")
print("-"*40)
itens = ("Lápis", 1.75,
         "Borracha", 2,
         "Caderno", 15.90,
         "Estojo", 25,
         "Corretivo", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Canetas", 22.30,
         "Livro", 34.90)
for c in range(0, len(itens)):
    if c % 2 == 0:
        print(f"{itens[c]:.<30}", end="")
    else:
        print(f"R$ {itens[c]:>7.2f}")
print("-"*40)
