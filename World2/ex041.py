#Classificação por idade
#----------

from datetime import date
atual = date.today().year
nasc = int(input("Diga o ano em que nasceu:"))
idade = atual - nasc

if idade <= 14:
    print("Apto para buscar a faixa verde.")
elif idade <= 18:
    print("Apto para buscar a faixa azul.")
else:
    print("Apto para buscar a faixa preta.")
#print(idade)
