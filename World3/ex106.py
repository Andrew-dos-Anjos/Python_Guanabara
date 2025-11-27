#Sistema interativo de ajuda em Python
# ----------

from time import sleep
c = ('\33[m',     # O - sem cores
     '\33[41m',   # 1- vermelho
     '\33[42m',   # 2 - verde
     '\33[43m',   # 3- amarelo
     '\33[44m',   # 4 - azul
     '\33[45m',   # 5 - roxo
     '\33[7;30m'  # 6 - branco
     )


def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'", 4)
    print(c[6], end="")
    help(com)
    print(c[0], end="")
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f" {msg}")
    print("~" * tam)
    print(c[0], end="")
    sleep(1)


comando = ""
while True:
    titulo( "SISTEMA DE AJUDA PyHELP", 2)
    comando = input("Função ou Biblioteca > ")
    if comando.upper() == 'FIM':
        break
    else:
        ajuda (comando)
titulo("ATÉ LOGO!", 1)
