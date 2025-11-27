#Aluguél de carros: um carro alugado custa R$60,00/dia e R$0,15/Km. Elabore o cálculo
#----------

dia = int(input("Por quantos dias usou o carro?"))
km = float(input("Quantos Kms percorreu?"))
print(f"O total a pagar de aluguél por {dia} dia(s) e {km}km(s) de uso é de R${dia*60 + km*0.15:.2f}")
