#Arquivos com Python
# ----------

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("Oção 2")
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\33[31mERRO! Digite uma opção válida\33[m")
    sleep(2)
