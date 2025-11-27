#Extensão .__trunc__()
#----------

'''import math
truco = float(input("Digite um número com decimais:"))
print(f"Número digitado: {truco} \nParcela inteira: {math.trunc(truco)}")'''

from math import trunc
truco = float(input("Digite um número com decimais:"))
print(f"Número digitado: {truco} \nParcela inteira: {truco.__trunc__()}")
#ou truco.trunc
