#Estatísticas em produtos
# ----------

total = mil = menor = cont = 0
barato = ""
while True:
    cont += 1
    produto = input("Informe o nome da mercadoria:")
    preco = float(input(f"Quanto custa um(a) {produto}: R$"))
    total += preco
    if preco >= 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar [S/N]:").upper()
    if continuar == "N":
        break
print(f"O total deu R${total:.2f}, tiveram {mil} produtos acima de mil R$ e o item mais barato foi o(a) {barato} de R${menor:.2f}.")
