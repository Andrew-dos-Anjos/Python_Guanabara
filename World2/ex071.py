#Simulador de caixa eletrônico
# ----------

#l = 50, xx = 20, x = 10, v = 5, i = 1
l = xx = x = v = i = 0
all = saque = int(input("Informe o valor do saque: R$"))
end = str(256 * "\033[1;;42m|$😔🫰$|\033[m")
while True:
    #50
    if saque >= 50:
        l = saque // 50
        if saque % 50 == 0:
            print(f"Seu saque de R${all} está disponível em {l} cedula(s) de R$50. \n{end}")
        else:
            saque = saque - (l*50)
    #20
    if 49 >= saque >= 20:
        xx = saque // 20
        if saque % 20 == 0:
            print(f"Seu saque de R${all} está disponível em {l} cedula(s) de R$50 e {xx} cedula(s) de R$20. \n{end}")
        else:
            saque = saque - (xx*20)
    #10
    if 19 >= saque >= 10:
        x = saque // 10
        if saque % 10 == 0:
            print(f"Seu saque de R${all} está disponível em {l} cedula(s) de R$50, {xx} cedula(s) de R$20 e {x} cedula de R$10. \n{end}")
        else:
            saque = saque - (x*10)
    #5
    if 9 >= saque >= 5:
        v = saque // 5
        if saque % 5 == 0:
            print(f"Seu saque de R${all} está disponível em {l} cedula(s) de R$50, {xx} cedula(s) de R$20, {x} cedula de R$10 e {v} cedula de R$5. \n{end}")
        else:
            saque = saque - (v*5)
    #1
    if 4 >= saque:
        i = saque // 1
        print(f"Seu saque de R${all} está disponível em {l} cedula(s) de R$50, {xx} cedula(s) de R$20, {x} cedula de R$10, {v} cedula de R$5 e {i} cedulas de R$1. \n{end}")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja realizar outro saque? [S/N]:").upper())
    if continuar == "S":
        all = saque = int(input("Informe a quantia do novo saque: R$"))
    else:
        break
