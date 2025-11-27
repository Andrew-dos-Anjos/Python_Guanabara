#Cadastro de Jogador de Futebol
# ----------

dicionario = {'nome': str(input("Nome do jogador:"))}
partidas = int(input("Número de partidas:"))
gols = []
total = 0
for c in range(partidas):
    gols.append(int(input(f"Gols marcados na {c + 1}° partida:")))
    total += gols[c]
dicionario['gols'] = gols
dicionario['total'] = total
print("-="*20)

print(dicionario)
print("-="*20)

for k, v in dicionario.items():
    print(f"O campo {k} tem valor {v}")
print("-="*20)

print(f"O jogador {dicionario['nome']} jogou {partidas} partidas:")
for i, v in enumerate(gols):
    print(f"=> Na {i + 1}° partida, marcou {v} gols;")
print(f"Foram o total de {total} gols.")
