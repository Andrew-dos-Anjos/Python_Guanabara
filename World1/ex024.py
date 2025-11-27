#Verificando as primeiras letras
#----------

cidade = str(input("Informe a sua cidade:")).lstrip()
#.lstrip() para retirar os espaços a esquerda.
print(cidade[:5].capitalize() == "Santo")
#[:5] para epecificar até o 5° caractere && .capitalize() para caso seja escrito "santo" ou "SaNtO";
#Nesse caso especifico poderia ser utilizado o .title(), mas o .capitalize() é mais indicado.
