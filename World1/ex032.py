#Ano bissexto
#----------

from datetime import date #datetime para ver a data e hora.
ano = int(input("Qual ano deseja analizar? Press 0 to ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto.")
else:
    print(f"O ano de {ano} não é bissexto.")
