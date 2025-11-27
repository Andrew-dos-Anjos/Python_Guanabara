#Função de Contador
# ----------

from time import sleep


def para(i, f, p):
    print(f"{'-='*20} \nContagem de {i} até {f} de {p} em {p}")
    if p < 0:
        f -= 1
    else:
        f += 1
    for c in range(i, f, p):
        print(c, end=" ")
        sleep(0.5)
    print("Fim!")


para(1, 10, 1)
para(10, 0, -2)
print(f"{'-=' * 20} \nSua vez de personalizar a contagem!")
para(int(input("Início: ")),
     int(input("Final:  ")),
     int(input("Passo:  ")))
