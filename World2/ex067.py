#Tabuada 3.0
# ----------

while True:
    n = int(input("Digite um número:"))
    if n <= 0:
        print("Finalizado.")
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {c*n}")
    print(17*"-")
