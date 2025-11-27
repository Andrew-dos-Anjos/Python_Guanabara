#Maior e menor valores em Tupla
# ----------

from random import randint
x = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(x)
print("Maior valor sorteado:", max(x), "Menor valor:", min(x))

#Para mostrar os números fora dos ():
'''for c in x:
     print(c, end=" ")'''
