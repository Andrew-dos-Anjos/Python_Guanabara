#Transformando módulos em pacotes
# ----------
from A22exs.utilidadescev import moeda

p = float(input("Informe é o preço do produto: R$"))
moeda.resumo(p, 20, 10)
