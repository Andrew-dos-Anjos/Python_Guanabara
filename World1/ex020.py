#Sorteio_2
#----------

import random

a = input("(1/4)Informe um nome a ser ordenado: ")
b = input("(2/4)Informe um nome a ser ordenado: ")
c = input("(3/4)Informe um nome a ser ordenado: ")
d = input("(4/4)Informe um nome a ser ordenado: ")
nomes = [a, b, c, d]
random.shuffle(nomes)
print("A ordem ficou: ", nomes)
