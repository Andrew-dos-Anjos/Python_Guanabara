#Números primos
# ----------

num = int(input("Digite um número:"))
cont = 0
for c in range(num, 0, -1):
    if num % c == 0:
        print("\33[32m", end="")
        cont += 1
    else:
        print("\33[37", end="m")
    print(c, end=" ")
print("\33[m", end="--> ")
if cont == 2:
    print("Número primo")
else:
    print("Número tio")
print(cont)
