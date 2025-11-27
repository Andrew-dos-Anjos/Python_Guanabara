#Unindo dicionários e listas
# ----------

mulher = {'mulher': []}
nome = []
gen = []
idade = []
i = total = cont = media = 0
while True:
    n = str(input("Nome:"))
    nome.append(n)
    mf = str(input("Genero[M/F]:"))
    while mf not in "MmFf":
        print("Erro!")
        mf = str(input("Favor especificar genero com [M/F]:"))
    if mf in "Ff":
        mulher['mulher'] = n
    gen.append(mf)
    i = int(input("Idade:"))
    total += i
    idade.append(i)
    cont += 1
    media = total/cont
    continua = input("Quer continuar? [S/N]:")
    while continua not in "SsNn":
        print("Erro!")
        continua = input("Favor especificar se quer continuar com [S/N]:")
    if continua in "Nn":
        break
    else:
        pass
dicionario = {'nome': nome, 'gen': gen, 'idade': idade}
print(f"A) Ao todo foram cadastradas {cont} pessoas.\n"
      f"B) A média de idade é {media:5.2f} anos.\n"
      f"C) As mulheres cadastradas foram ")
for p in mulher['mulher']:
    print(p, end=" ")
print(f"D) Lista de pessoas com idade acima da média:")
for i in idade:
    if idade[i] >= media:
        print("   ", end="")
        for k, v in dicionario.items():
            print(f"{k} == {v}; ", end="")
        print()
#if dicionario['pessoas'][1] > media:
