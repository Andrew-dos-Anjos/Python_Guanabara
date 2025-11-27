#Dicionário em Python
# ----------

#nome, media (rep5, rec.., apr7), situaçao

dicionario = {'nome': str(input("Nome do aluno:"))}
m = dicionario['media'] = float(input(f"Média:"))
print("-="*15)
for k, v in dicionario.items():
    print(f" -{k} do aluno: {v}")
s = dicionario['situacao'] = ("Reprovado", "Recuperação", "Aprovado")
if m < 5:
    print(f" -{s[0]}")
elif m < 7:
    print(f" -{s[1]}")
else:
    print(f" -{s[2]}")
