#Procurando uma string dentro de outra
#----------

nome = input("Diga seu nome completo:").title()  #.strip() opcional
#.title para colocar cada inicial em maiúsculo.
print("Seu nome tem Ferreira?", "Ferreira" in nome)
#O operador "<str>" in var retorna Verdadeiro(T) se encontrar a string especificada &&
#Flso(F) se não encontrar.
