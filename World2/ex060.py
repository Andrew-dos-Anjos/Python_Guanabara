#Cálculo do fatorial
# ----------

num = int(input("Número:"))
fat = 1
print(f"{num}! = {num} ", end="")
while num > 0:
    print(f"x {num-1} " if num > 1 else "= ", end="")
    fat *= num
    num -= 1
print(fat)
