#Lista ordenada sem repetições
# ----------

cinco = []
for c in range(0, 5):
    num = int(input("Digite um valor:"))
    if c == 0 or num >= cinco[-1]:
        cinco.append(num)
        print("Adicionado ao final da lista!")
    else:
        posicao = 0
        while posicao < len(cinco):
            if num < cinco[posicao]:
                cinco.insert(posicao, num)
                print("Adicionado na posição:", posicao)
                break
            posicao += 1
print(cinco)
