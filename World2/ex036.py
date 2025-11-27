#Aprovando Empréstimo
#----------

casa = float(input("Quanto custa a casa a venda? R$:"))
sal = float(input("Quanto você ganha mensalmente? R$:"))
ano = int(input("Quantos anos para a quitar a divida? "))
mes = ano*12
pag = casa/mes

if pag > (sal*30/100):
    print("Empréstimo negado. "
          f"O mínimo para obtenção do crédito é de R${pag*3.34:.2f}")
else:
    print("Empréstimo concedido.")
#print((sal*30/100))
#print(pag)
