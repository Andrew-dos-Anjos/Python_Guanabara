#Boletim com listas compostas
# ----------

aluno = list()
while True:
    nome = str(input(f"Nome do aluno: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    aluno.append([nome, [n1, n2], media])

    continua = input("Quer continuar? [S/N]:")
    while continua not in "SsNn":
        continua = input("Quer continuar? [S/N]:")
    if continua in "Nn":
        print("-="*25)
        break
print(f"{"N°":<4}{"Nome":<10}{"Média":>8}")
print("-"*22)
for i, a in enumerate(aluno):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-"*30)
    opc = int(input("Deseja mostrar as notas de um aluno? (999 para finalizar):"))
    if opc == 999:
        print("Encerrado!")
        break
    elif opc <= len(aluno) - 1:
        print(f"Notas de {aluno[opc][0]}: {aluno[opc][1]}")
