#Um print especial
# ----------

def escreva(frase):
    print("~"*len(frase) + "~~")
    print(f" {frase}")
    print("~"*len(frase) + "~~")


escreva(input("Diga algo: "))
