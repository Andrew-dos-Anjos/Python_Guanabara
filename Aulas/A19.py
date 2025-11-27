#16:30
dicionario = dict()
pessoa = {'nome': "Drew", 'idade': 20, 'gen': "Rock🤘"}
#Seria o equivalente a {pessoa[0]}, {pessoa[1]} numa lista.
print(f"O {pessoa['nome']} tem {pessoa['idade']} anos")
#Para copiar um dicionário:
pessoa.copy()
print()

filme = {'titulo': "O rei leão",
         'ano': 1994,
         'produtora': "Disney™"
         }
print(filme)

locadora = list()
locadora.append(filme)
print(locadora[0].values())
print()

#Uma caracteristica com o laço for que se assemelha com o enumerate nas listas:
for k, v in filme.items():
    print(f"{k} = {v}")
print()

del filme['produtora']
print(filme.keys())
filme['nota'] = 10
print(filme.keys())
