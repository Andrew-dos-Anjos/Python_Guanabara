#Radar eletrônico
#----------

from random import random

radar = int(input("Você acaba de ultrapassar o radar de 80Km/hr. A qual velocidade você estava? "))
multa = int((radar-80) * 7)
if radar <= 80:
    print(f"{radar}Km. Safe")
elif 81 <= radar <= 90:
    margem = random()
    #print(margem)
    if margem <= 0.5:
        print(f"{radar}Km... O radar estava mal calibrado. Sortudo!")
    else:
        print(f"{radar}km... Mesmo assim pegou... Pague R${multa},00.")
else:
    print(f"{radar}Km! Sua multa é de R${multa},00 por excesso de velocidade.")
#O último "else" acima poderia ser simplificado escrevendo sua condição de forma direta em seu lugar
