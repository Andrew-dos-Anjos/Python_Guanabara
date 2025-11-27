#Função que descobre o maior
# ----------

from time import sleep


def maior(* num):
    c = m = 0
    print(f"{'-='*30}\nAnalizando os números...")
    for valor in num:
        print(f"{valor} ", end="", flush=True)
        sleep(0.3)
        if c == 0:
            m = valor
        elif valor > m:
            m = valor
        c += 1
    print(f"\nDos {c} valores apresentados, o maior é o {m}!")


maior(1, 2, 3, 4)
maior(4, 3, 2, 1)
maior(5, 4, 8, 4, 1)
maior(2)
maior()
