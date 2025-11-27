#Progressão aritmética
# ----------

num = int(input("Informe um número:"))
pa = int(input("Informe a PA:"))
soma = 0
for c in range(1, 11):
    print(num + soma, end=" ")
    soma += pa
