#Soma ímpares ×3-500
# ----------

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
#Usual: cont += 1 / soma += c
print(f"Ao todo foram {contador} números, que somados equivalem a = {soma}")
