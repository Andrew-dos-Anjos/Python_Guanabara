#Funções para sortear e somar
# ----------

from random import randint
from time import sleep


def sorteia(num):
    print("Sorteando os numéros...")
    sleep(2)
    for c in range(5):
        num.append(randint(1, 10))
        print(num[c], end=" ", flush=True)
    print()


def somapar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    sleep(1)
    print(f"Somando os pares de {num} o resultado é = {soma}")


numeros = []
sorteia(numeros)
somapar(numeros)
