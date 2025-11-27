#Calculo de descontos
#----------

prod = float(input("Informe o valor do produto:"))
print(f"O seguinte produto no cartão (com 5% de desc.) fica a: {prod-(prod*5/100):.2f}; "
      f"a vista (com 10%): {prod-(prod*10/100):.2f} "
      f"e em dinheiro (com 15%): {prod-(prod*15/100):.2f}")
