#Função que calcula área
# ----------

def calculo(comprimento, largura):
    area = comprimento * largura
    print(f"A área do terreno {comprimento}x{largura} é de: {area}m²")


print(f" Controle de terreno: \n{'-'*22}")
calculo(float(input("comprimento(m): ")),
        float(input("largura(m): ")))
