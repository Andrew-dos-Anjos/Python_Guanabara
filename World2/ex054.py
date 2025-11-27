#Maioridade.2
# ----------

from datetime import date
hoy = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input(f"Qual o ano de nascimento da {c}ª pessoa?"))
    idade = hoy - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f"{menor}🔞{maior}😈")
