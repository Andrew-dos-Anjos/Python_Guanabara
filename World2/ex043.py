#Índice de Massa Corporea
#----------

altura = float(input("Qual é a sua altura?"))
peso = float(input("Qual é o seu peso?"))
imc = peso/(altura**2)

print(f"Seu IMC é de:{imc:.2f}\nCategoria: ", end="")
if imc < 18.5:
    print("Peso pena")
elif imc <= 25:
    print("Magrin")
elif imc <= 30:
    print("Médio")
elif imc <= 40:
    print("Pesado")
else:
    print("Lutador de sumo!")
