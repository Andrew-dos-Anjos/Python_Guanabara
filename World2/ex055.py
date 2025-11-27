#Maior e menor sequencia
# ----------

for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}ª pessoa?"))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"Menor {menor:.2f}Kg, maior {maior:.2f}Kg")
