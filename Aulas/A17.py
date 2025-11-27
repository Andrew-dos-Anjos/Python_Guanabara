#15:20
#[] vs list()
convocado = list("Lista, por, comando")
colchetes = ["lista", "p", "colchete", "XD!"]
print(convocado)  # Cada caractere ocupa um espaço na lista.
colchetes.pop()
colchetes.append("XDn't")
print(colchetes)  # Cada palavra por inteiro é considerada como item.
#A pricipal função da listagem por comando é de trnasformar outros parametros em lista.
#Para uso convencional é mais utilizado '[]'.
print()

#Leitura de valores incorporados:
valores = list()
for c in range(0, 4):
    valores.append(int(input("Digite um N°:")))

for p, v in enumerate(valores):
    print(f"Na posição {p} está o N°: {v}")
print("Gabarito =", valores)
print()

#Cópia vs ligação
a = [1, 2, 3, 4]
b = a
b[2] = 0  # [1, 2, 0, 4]
print(f"A{a} tem relação direta com B{b}")
#Para fazer uma cópia de uma lista:
c = [5, 6, 7, 8]
d = c[:]
d[0] = 10
print(f"Lista C:{c}\nLista D:{d}")
