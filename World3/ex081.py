#Extraindo dados de uma Lista
# ----------

num = [int(input("digite um numero:"))]
while True:
    continua = input("Quer continuar? [S/N]:")
    while continua not in "SsNn":
        continua = input("Quer continuar? [S/N]:")
    if continua in "Nn":
        break
    else:
        num.append(int(input("digite um numero:")))
print(f"Você digitou {len(num)} números;")
num.sort(reverse=True)
print(f"Números registrados em ordem decrescente: {num};")
#No caso como se trata apenas do valor 5, poderia escrito como: 'if 5 in num:'
if num.count(5) >= 1:
     print(f"A lista contem o N° 5.")
else:
     print(f"A lista não contem o N° 5.")
