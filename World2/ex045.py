# Pedra, Papel e TesoouuRA!
# ----------

#A importação time.sleep (l13 e l15) habilita pausas entre <str>
from time import sleep
from random import randint

print("1 = Pedra, 2 = Papel, 3 = Tesoura")
me = int(input("Escolha entre 1 e 3 para representar sua jogada:"))
cpu = randint(1, 3)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("CPU:", cpu)

if cpu == me:
    print("Empate")
else:
    #Pedra
    if me == 1:
        if cpu == 2:
            print("Perdeu.")
        elif cpu == 3:
            print("Ganhou.")
    #Papel
    elif me == 2:
        if cpu == 3:
            print("Perdeu.")
        elif cpu == 1:
            print("Ganhou.")
    #Tesoura
    elif me == 3:
        if cpu == 1:
            print("Perdeu.")
        elif cpu == 2:
            print("Ganhou.")

# Jo Ken Po!🏆
