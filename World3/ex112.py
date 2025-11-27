#Entrada de dados monetários
# ----------
from A22exs.utilidadescev import moeda
from A22exs.utilidadescev import dados

p = dados.leiadinheiro("Informe é o preço do produto: R$")
moeda.resumo(p, 20, 10)
