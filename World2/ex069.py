#Análise de dados do grupo
# ----------

homem = mulher20 = mais = 0
while True:
    age = int(input("Informe sua idade:"))
    gen = " "
    while gen not in "MF":
        gen = input("Informe o seu gênero [M/F]:").upper()
    if gen == "M":
        homem += 1
    if age >= 18:
        mais += 1
    if gen == "F" and age < 20:
        mulher20 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar [S/N]:").upper()
    if continuar == "N":
        break
print(f"+18: {mais}, Homens: {homem}, Mulheres(-20):{mulher20}")
