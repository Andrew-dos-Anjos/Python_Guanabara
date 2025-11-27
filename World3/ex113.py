#Funções aprofundadas em Python
# ----------

def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print("\33[31mErro! Por favor digite um número inteiro válido.\33[m")
            continue
        except (KeyboardInterrupt):
            print("\n\33[31mUsuário preferiu não informar o número\33[m")
            return 0
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print("\33[31mErro! Por favor digite um número real válido.\33[m")
            continue
        except (KeyboardInterrupt):
            print("\n\33[31mUsuário preferiu não informar o número\33[m")
            return 0
        else:
            return n


n1 = leiaInt("Digite um número inteiro:")
n2 = leiaFloat("Digite um número real:")
print(f"Real: {n1};\nInteiro: {n2}")
