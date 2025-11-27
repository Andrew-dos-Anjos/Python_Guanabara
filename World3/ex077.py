#Contando vogais em Tupla
# ----------

#Tupla
palavras = str("Vou"), str("almoçar"), str("na"), str("casa"), str("da"), str("minha"), str("mae")
#Cada elemento da tupla
for p in palavras:
    print(f"\nNa palavra \033[4m{p:<7}\033[m as vogais são:", end=" ")
    #Cada especificação dos elementos
    for letra in p:
        if letra in "aeiou":
            print(letra, end=" ")
