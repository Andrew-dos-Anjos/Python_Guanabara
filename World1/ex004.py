# Identificar o tipo da variável (Função “.is”)
#----------

var = input("Digite algo: ")
print("O tipo primitivo é:", type(var))

print("É alfabético?", var.isalpha())
print("É numérico?", var.isnumeric())
print("É alfanumérico?", var.isalnum())

print("É tudo maiúsculo?", var.isupper())
print("É tudo minúsculo?", var.islower())
print("É maiúsculo com minúsculo?", var.istitle())
                                        #Captalizada

print("É apenas 'Espaço'?", var.isspace())

#Específicos:
print("É 'mostravel'?", var.isprintable())
#A Identificar:
print("É um identificador válido em Python?(Conferir*)", var.isidentifier())
print("O que É??", var.isdecimal())
print("O que É??", var.isdigit())
print("O que É??", var.isascii())
