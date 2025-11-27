# Tratando vários valores
# ----------
num = int(input("Digite um número [0 para parar]"))
soma = num
while num != 0:
    num = int(input("Digite um número [0 para parar]"))
    soma += num
print("A soma dos números registrados  = ", soma)
