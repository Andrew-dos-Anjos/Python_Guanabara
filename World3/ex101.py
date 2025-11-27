#Funções para votação
# ----------

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        print(f"Com {idade} anos, não é permitido votar.")
    elif 18 <= idade < 65:
        print(f"Com {idade} anos, o voto é obrigatório.")
    else:
        print(f"Com {idade} anos, o voto é opcional.")


nasc = int(input("Diga o ano em que nasceu:"))
voto(nasc)
