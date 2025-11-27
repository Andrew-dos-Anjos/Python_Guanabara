#13min
l1 = [1, 2, 3]
l2 = l1[:]
l2.append(4)
cj = [l1, l2]
print(cj)
print()

turma = [["Jurandir", 2], ["Wimbledon", 4], ["Vanderlei", 3], ["Charles", 1]]
turma.sort()
for c in turma:
    print(f"Aluno: {c[0]}, N° da chamada {c[1]}")
print()

bdd = list()
dado = list()
while True:
    dado.append(str(input("Digite o nome (0 para finalizar):")))
    if dado[0] == "0":
        break
    dado.append(str(input("Idade:")))
    bdd.append(dado[:])
    dado.clear()
print("Informações armazenadas:\n", bdd)
