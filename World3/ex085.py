#Listas com pares e ímpares
# ----------

poui = [[], []]
for c in range(0, 7):
    num = int(input(f"Digite o {c+1}° número:"))
    if num == 0:
        pass
    elif num % 2 == 0:
        poui[0].append(num)
    else:
        poui[1].append(num)
poui[0].sort()
poui[1].sort()
print(f"Pares: {poui[0]} \nÍmpares: {poui[1]}")
