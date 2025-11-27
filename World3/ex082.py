#Dividindo valores em várias listas
# ----------

num = [int(input("Digite um número:"))]
pares = list()
impares = list()
while True:
    continua = input("Quer continuar? [S/N]:")
    while continua not in "SsNn":
        continua = input("Quer continuar? [S/N]:")
    if continua in "Nn":
        break
    else:
        num.append(int(input("Digite um número:")))
print("Lista:", num)
for p, n in enumerate(num):
    if n == 0:
        pass
    elif n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f"Lista de Pares: {pares} \nLista de Impares: {impares}")
