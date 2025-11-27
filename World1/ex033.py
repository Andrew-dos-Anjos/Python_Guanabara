#Maior e menor valor
#----------

n1 = int(input("Digite o 1° número:"))
n2 = int(input("Digite o 2° número:"))
n3 = int(input("Digite o 3° número:"))
print(f"Números digitados {n1}, {n2} e {n3}.")
#Menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#Maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
#Com as variáveis adicionais o caminho a percorrer fica mais curto uma vez que as alternativas são pressupostas e
#podem ser redefinidas postumamente.
print(f"Menor valor:{menor} \nMaior valor:{maior}")
