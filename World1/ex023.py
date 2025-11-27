#Separando digitos de um número
#----------

num = int(input("Informe um número entre 0 a 9999:"))

u, d, c, m = num // 1 % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10
#A divisão inteira para isolar o número e o resto para ignorar os demais. Ex.:
#Para encontrar a centena: 1234 // 100 == 12 ... 12 % 10 == 2.
print(f"O número {num} tem: \nUnidades de milhar:{m}  \nCentenas:{c}  "
      f"\nDezenas:{d}  \nUnidades:{u} ")

#Se fosse certeza que seria apresentado um número de 4 digitos (entre 1000 e 9999),
#o código poderia ser feito por manipulação de <str> sem precisar do <int>. Ex.:
#print(f"O número {num} tem: \nUnidades de milhar:{num[0]}  \nCentenas:{num[1]}  "
#      f"\nDezenas:{num[2]}  \nUnidades:{num[3]} ")
