#Jogo de Dados em Python
# ----------

from random import randint
from time import sleep
#Importação:
from operator import itemgetter

num = int(input("Quantos jogadores vão participar? (N°):"))
dicionario = {}
ranking = list()
print("Rolando os dados...")
for c in range(num):
    dicionario[f'Jogador{c + 1}'] = randint(1,6)
for k, v in dicionario.items():
    sleep(1)
    print(f"{k} == {v}")
sleep(2)
#Função:
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print("-=-"*10)
print("    == Ranking 🏆 ==")
for i, v in enumerate(ranking):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}.")
