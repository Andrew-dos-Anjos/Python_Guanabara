#Validando entrada de dados em Python
# ----------

def leiaInt(num):
    valor = 0
    while True:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print("\33[31mErro! Digite um número inteiro válido.\33[m")
    return valor


n = leiaInt("Digite um número:")
print(f"Você digitou o número: {n}")
