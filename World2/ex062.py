#Progressão aritmética 3.0
# ----------

num = int(input("Informe um número:"))
pa = int(input("Informe a PA:"))
soma = 0
c = 1
num2 = 10
total = 0

while num2 != 0:
    total += num2
    while c <= total:
        print(num + soma, end=" > ")
        soma += pa
        c += 1
    print("Pausa")
    num2 = int(input("Quantos termos deseja acrescentar?"))
print(f"Processo finalizado com {total} termos apresentados.")
