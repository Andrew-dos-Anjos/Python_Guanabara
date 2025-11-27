#Conversor de moedas
#----------

real = float(input("Quantos reais você tem? R$:"))
print(f"Com R$${real:.2f}; você pode comprar {real/5:.2f} dolares, {real/5.5:.2f} euros,"
      f"{real/0.005:.2f} kwanzas e {real/15000:.6f} ethereum")
