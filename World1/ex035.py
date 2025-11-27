#Analisando triângulo 1.0
#----------

reta1 = float(input("Informe o comprimento da 1ª reta:"))
reta2 = float(input("Informe o comprimento da 2ª reta:"))
reta3 = float(input("Informe o comprimento da 3ª reta:"))

if reta1 + reta2 >= reta3 and reta1 + reta3 >= reta2 and reta2 + reta3 >= reta1:
    print("As medidas fornecidas podem formar um triângulo.")
else:
    print("Não é possível formar um triângulo com essas medidas.")
