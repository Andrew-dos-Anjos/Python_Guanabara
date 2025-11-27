#Vários números com flag
# ----------

c = soma = 0
while True:
    num = int(input("Digite um N°:"))
    if num == 999:
        break
    c += 1
    soma += num
print(f"Os {c} valores somam = {soma}")
