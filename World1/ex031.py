#Custo da viagem
#----------

d = float(input("Diga a distância da sua viagem (em Km) para ser calculado o valor da passagem:"))
'''if d <= 200:
    preço = d*0.50
else:
    preço = d*0.45'''
#Forma simplificada:
preço = d*0.5 if d<=200 else d*0.45
print(f"O valor da sua passagem é de: R${preço:.2f}")
