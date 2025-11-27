#Sorteio
#----------

import random

a = input("(1/4)Informe um nome a ser sorteado: ")
b = input("(2/4)Informe um nome a ser sorteado: ")
c = input("(3/4)Informe um nome a ser sorteado: ")
d = input("(4/4)Informe um nome a ser sorteado: ")
nomes = [a, b, c, d]
#Para listas usam-se os colchetes []
print("O nome sorteado foi:", random.choice(nomes))
