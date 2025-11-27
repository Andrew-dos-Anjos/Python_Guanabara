#Número por Extenso
# ----------

extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
           "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
           "Doze", "Treze", "Catorze", "Quinze", "Dezesseis",
           "Dezessete", "Dezoito", "Dezenove", "Vinte")
num = int(input("Digite um número entre 0 e 20: "))
while num not in range(21):
    num = int(input("Por favor, digite um número \033[31mentre 0 e 20\033[m: "))
print("O número digitado foi:", extenso[num])
