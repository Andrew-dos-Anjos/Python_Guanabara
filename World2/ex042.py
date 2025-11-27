#Analisando triângulo 2.0
#----------

l1 = int(input("Informe o tamanho do 1° lado:"))
l2 = int(input("Informe o tamanho do 2° lado:"))
l3 = int(input("Informe o tamanho do 3° lado:"))

if l1 + l2 >= l3 and l1 + l3 >= l2 and l2 + l3 >= l1:
    if l1 == l2 == l3:
        print("Triângulo equilatero.")
    elif l1 != l2 != l3 != l1:
        #O 'l1' foi especificado mais uma vez pois é necessário para comparação com o 'l3'.
        print("Triângulo escaleno.")
    else:
        print("Triângulo isósceles.")
else:
    print("As medidas fornecidas não podem formar um triângulo.")
