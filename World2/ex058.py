# Jogo da Adivinhação v2.0
# ----------

from random import randint

num = randint(0, 10)
win = False
while not win:
    sort = int(input("Escolha um número de 0 a 10:"))
    if sort < num:
        print("Maior")
    elif sort > num:
        print("Menor")
    else:
        win = True
print(num)
print("Acertou!")
