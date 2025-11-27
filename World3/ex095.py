#Aprimorando os Dicionários
# ----------

#cod, nome, gols, total. levantamento
gols = []
rep = total = 0
while True:
    dicionario = {f'nome{rep}': str(input("Nome do jogador:"))}
    partidas = int(input("Número de partidas:"))
    for c in range(partidas):
        gols.append(int(input(f"Gols marcados na {c + 1}° partida:")))
        total += gols[c]
    dicionario[f'gols{rep}'] = gols
    dicionario[f'total{rep}'] = total
    continua = input("Quer continuar? [S/N]:")
    while continua not in "SsNn":
        continua = input("Quer continuar? [S/N]:")
    if continua in "Nn":
        break
    else:
        del gols[0:]
        rep += 1
print("-="*20)

print(f"cod nome            gols            total\n{"-"*20}")
for c in range(rep):
    print(f" {c}  {dicionario[f'nome{c}']}    {dicionario[f'gols{c}']}    {dicionario[f'total{c}']}")

'''print(f"O jogador {dicionario['nome']} jogou {partidas} partidas:")
for i, v in enumerate(gols):
    print(f"=> Na {i + 1}° partida, marcou {v} gols;")'''
