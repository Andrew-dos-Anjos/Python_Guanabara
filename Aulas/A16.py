#21min
lanche = ("hamburguer", "suco", "pizza", "pudim") #a partir da versão 3.5 não há a necessidade do uso de '()'
print(lanche)
#lanche[1] = "refri"
#A linha acima não altera o valor inicial pelo princípio da imutalidade.
print(lanche[1])
print(lanche[-1])
#Especificando com um N° negativo a demonstração do termo conta da direita para a esquerda.
print(sorted(lanche))
#Função sorted deixa em ordem transformando a Tupla em Lista.
print()
#27min
#Para STRs o laço for pode ser usado das seguintes formas:
for comida in lanche:
    print(f"Eu comi {comida}")
print()
for c in range(0, len(lanche)):
    print(f"Eu comi {lanche[c]}")
print()
for cont, comida in enumerate(lanche):
    print(f"Eu comi {comida} na posição {cont}")
print("\033[4mUm prato de cada vez!\033[m")
print()
#36min
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(f"C: {c}\nD: {d} qnt de valores na tupla ", len(d))

print("Quantas vezes o num 5 aparece em c: ", c.count(5))
print("Em qual posição o num 5 aparece em c a partir da colocação 2: ", c.index(5, 2))
print()
#Também é possível guardar valores com mais de um tipo primitivo numa Tupla.
pessoa = ("Andrew", 20, "M", 67.5)  # Nome, idade, sex, peso.
print(pessoa)
#Apesar de não poder ser mudada é possível deletar a Tupla
del pessoa
#print(pessoa) Não apresentará nenhum valor!
