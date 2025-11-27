#Exercitando módulos em Python
# ----------
from A22exs import moeda

p = float(input("Informe é o preço do produto: R$"))
print(f"O dobro de R${p} é {moeda.dobro(p)}")
print(f"A metade de R${p} é {moeda.metade(p)}")
print(f"R${p} com 10% a mais fica R${moeda.aumentar(p, 10)}")
print(f"R${p} com 20% a menos fica R${moeda.diminuir(p, 20)}")
