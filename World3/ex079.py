#Valores únicos em uma Lista
# ----------

num = [int(input("digite um numero:"))]
while True:
    continua = input("Quer continuar? [S/N]:")
    while continua not in "SsNn":
        continua = input("Quer continuar? [S/N]:")
    if continua in "Nn":
        print("Números registrados:", sorted(num))
        break
    else:
        novonum = (int(input("digite um numero:")))
        if novonum in num:
            print("Valor já registrado!")
        else:
            num.append(novonum)
