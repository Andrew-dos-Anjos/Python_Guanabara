# Validação de Dados
# ----------

s = str(input("Informe o seu sexo [M/F]: ")).upper()
while s not in "MF":
    s = input("\33[;31mInvalido!\33[m Selecione uma das alternativas [M/F]").upper()
if s == "M":
    print("Homem")
if s == "F":
    print("Mulher")
