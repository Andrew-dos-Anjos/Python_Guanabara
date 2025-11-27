#Aumentos múltiplos
#----------

sal = float(input("Qual é o valor do seu sálario atual? R$:"))

if sal <= 1250:
    up = sal+(sal*15/100)
else:
    up = sal+(sal*10/100)
print(f"Seu novo salário é de R${up:.2f}")

#!Reformular com a importação math.pow
