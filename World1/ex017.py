#Trigonometria
#----------

co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
#hi = (co**2 + ca**2)**(1/2)
from math import hypot
hi = hypot(ca, co)
print(f"Comprimento da hipotenusa: {hi:.2f}")
