#Formatando Moedas em Python
# ----------
from A22exs import moeda

p = float(input("Informe é o preço do produto: R$"))
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"{moeda.moeda(p)} com 10% a mais fica {moeda.moeda(moeda.aumentar(p, 10))}")
#Sem formatação:
print(f"{p} com 20% a menos fica {moeda.diminuir(p, 20)}")
