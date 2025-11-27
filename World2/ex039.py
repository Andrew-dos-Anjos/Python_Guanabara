#Alistamento militar
#----------

from datetime import date
atual = date.today().year
nasc = int(input("Diga o ano em que nasceu:"))
idade = atual - nasc

if idade < 18:
    print(f"Com {idade} anos você ainda não pode se alistar, "
          f"espere mais {18 - idade} ano(s).")
        #ou"espere até {18 - idade + atual}."
elif idade == 18:
    print("Você completa 18 anos esse ano, tem a obrigação de se apresentar.")
else:
    print(f"Com {idade} anos se você ainda não se alistou, deve se apresentar o quanto antes!")
