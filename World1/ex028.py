#Choose game
#----------

from random import randint

d5 = randint(1, 5)
c = int(input("Escolha um número de 1 a 5:"))
print("O número deu:", d5)
if c == d5:
    print(f"Seu número ({c}), você venceu!")
else:
    print(f"Seu número ({c}), você perdeu.")

'''d1 = randint(1, 6)
d2 = randint(1, 6)
r = int(d1+d2)
num = int(input("Aposte 6 se acha que os dados vão somar juntos menos que 7; 7 = 7 ou 8 mais que 7:"))
print(f"Seu número: {num} \nDado_1: {d1} \nDado_2: {d2} \nResultado: {r}")
if num <= r & r < 7:
    print("Ganhou +50$$")
elif num >= r & r > 7:
    print("Ganhou +50$$")
elif num == 7 & r == 7:
    print("Ganhou +100$$")
else:
    print("A casa Ganhou $͜$")'''
#Cassino🏆

'''porta = int(input("Digite '1', '2' ou '3' para escolher uma das três portas:"))
print(f"Atrás da porta N° {porta} tem...", end=" ")
if porta == 1:
    print("Ha!")
elif porta == 2:
    print("IeIe!")
elif porta == 3:
    print("Um Macaco!")
else:
    print("Por favor, Digite '1', '2' ou '3'. Seu macaco XD")'''
#Olha o Macaaaaco!🏆
