#Formatando Moedas em Python
# ----------
from A22exs import moeda

p = float(input("Informe é o preço do produto: R$"))
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"Com 10% a mais fica {moeda.aumentar(p, 10, True)}")
#Sem retornar o formato como True
print(f"Com 20% a menos fica {moeda.diminuir(p, 20)}")
