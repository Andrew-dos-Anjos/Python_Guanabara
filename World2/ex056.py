#Analisador completo
# ----------

soma = 0
media = 0
velho = 0
homem = ""
cont = 0
for c in range(1, 5):
    print(f"----- {c}ª pessoa -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    soma += idade
    sex = str(input("Sexo[M/F]: ")).strip()
    if c == 1 and sex in "Mm":
        velho = idade
        homem = nome
    if sex in "Mm" and idade > velho:
        velho = idade
        homem = nome
    if sex in "Ff" and idade < 20:
        cont += 1
media = soma / 4
print(f"A média das idades é: {media}\n"
      f"O {homem} é O mais velho e tem {velho} anos\n"
      f"E ao todo há {cont} mulher(es) abaixo de 20 anos.")
#Revisar
