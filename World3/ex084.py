#Lista composta e análise de dados
# ----------

nomepeso = [input("Informe o nome: "), int(input("Informe o peso em Kg: "))]
listao = [nomepeso[:]]
menor = maior = nomepeso[1]
nomepeso.clear()
while True:
    continua = input("Quer continuar? [S/N]:")
    while continua not in "SsNn":
        continua = input("Quer continuar? [S/N]:")
    if continua in "Nn":
        print(f"Pessoas cadastradas: {listao} \nMenor peso: {menor}Kg, pessoas:")
        for p in listao:
            if menor == p[1]:
                print(f"{p[0]};", end=" ")
        print(f"\nMaior peso: {maior}Kg, pessoas:")
        for p in listao:
            if maior == p[1]:
                print(f"{p[0]};", end=" ")
        break
    else:
        nomepeso = [input("Informe o nome: "), int(input("Informe o peso em Kg: "))]
        listao.append(nomepeso[:])
        if menor > nomepeso[1]:
            menor = nomepeso[1]
        if maior < nomepeso[1]:
            maior = nomepeso[1]
        nomepeso.clear()
