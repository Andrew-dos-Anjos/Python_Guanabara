#Maior e Menor valores na Lista
# ----------

cinco = list()
menor = maior = 0
for c in range(0, 5):
    cinco.append(int(input("Digite um número:")))
    #O primeiro 'if' é essencial para definir as var 'maior' e 'menor'.
    if c == 0:
        menor = maior = cinco[c]
    if menor > cinco[c]:
        menor = cinco[c]
    if maior < cinco[c]:
        maior = cinco[c]
print(f"Lista:{cinco} \nMenor valor: {menor}. Aparece em ", end="")
for p, n in enumerate(cinco):
    if n == menor:
        print(f"{p};", end=" ")
print(f"\nMaior valor: {maior}. Aparece em ", end="")
for p, n in enumerate(cinco):
    if n == maior:
        print(f"{p};", end=" ")
