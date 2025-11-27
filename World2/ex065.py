#Maior e maior valores
# ----------

num = int(input("Digite um número:"))
maior = menor = num
soma = num
cont = 0
while num != 0:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input("Digite outro número ou '0' para interromper:"))
    soma += num
    cont += 1
media = soma/cont
print(f"Maior: {maior} Menor: {menor} Média: {media}")
