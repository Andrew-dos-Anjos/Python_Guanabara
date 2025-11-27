style = {"normal":"\033[0m", "negrito":"\033[1m", "underline":"\033[4m", "negativo":"\033[7m"}
text = {"neutro":"\033[30m", "vermelho":"\033[31m", "verde":"\033[32m", "amarelo":"\033[33m",
        "azul":"\033[34m", "roxo":"\033[35m", "azul2":"\033[36m", "cinza":"\033[37m"}
back = {"neutral":"\033[40m", "red":"\033[41m", "green":"\033[42m", "yellow":"\033[43m",
        "blue":"\033[44m", "purple":"\033[45m", "blue2":"\033[46m", "gray":"\033[47m"}
clean = "\033[m"

print(f"{text['azul']}frase{clean}")
