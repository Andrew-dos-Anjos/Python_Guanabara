#Análise de dados em uma Tupla
# ----------

num = (int(input("Digite o 1° número:")), int(input("Digite o 2° número:")),
       int(input("Digite o 3° número:")), int(input("Digite o 4° número:")))
print(num)
print("Vezes em que o N° 9 aparece:", num.count(9))
if 3 in num:
    print("Primeira posição em que o N° 3 aparece:", num.index(3))
else:
    print("Não há nenhum 3.")
print("Par:", end=" ")
for c in num:
    if c % 2 == 0:
        print(c, end=" ")
