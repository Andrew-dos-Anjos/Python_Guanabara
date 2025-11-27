#Par ou ímpar 🎮
# ----------

from random import randint

c = 0
while True:
    pc = randint(1,2)
    num = int(input("Escolha um número:"))
    poui = num + pc
    play = input("Escolha Par ou Ímpar [P/I]:").upper()
    if play == "P" and poui % 2 == 0:
        print(f"(You)  (CPU)\n  {num}  ++  {pc}  =  {poui} Par!\n-", 10*"- ")
    elif play == "I" and poui % 2 == 1:
        print(f"(You)  (CPU)\n  {num}  ++  {pc}  =  {poui} Ímpar!\n-", 11*"- ")
    else:
        if poui % 2 == 0:
            print(f"(You)  (CPU)   Score|{c}|\n  {num}  ++  {pc}  =  {poui} Par!\nGame Over")
        elif poui % 2 == 1:
            print(f"(You)  (CPU)   Score|{c}|\n  {num}  ++  {pc}  =  {poui} Ímpar!\nGame Over")
        break
    c += 1
