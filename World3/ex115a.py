#Criando um menu em Python
# ----------

from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        cabeçalho("Oção 1")
    elif resposta == 2:
        cabeçalho("Oção 2")
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\33[31mERRO! Digite uma opção válida\33[m")
    sleep(2)
