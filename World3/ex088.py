#Palpites para a Mega Sena
# ----------

from random import randint
from time import sleep
jogo = list()
jogos = list()
quant = int(input("Quantos jogos deseja?: "))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    total += 1
print(f"=-=Sorteando {quant} jogos=-=")
sleep(1)
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print("-=-Boa $orte!-=-")
