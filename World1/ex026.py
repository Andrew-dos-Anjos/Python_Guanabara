#Primera e última aparição de um caractere <str>
#----------

frase = str(input("Diga uma frase:")).strip().upper()
#.strip tira os espaços iniciais e finais && .upper() deixa tudo em miúsculo.
print("A letra A aparece", (frase.count("A")), "vezes na frase.")
#Com a frase toda em maiúsculo, o .count("A") consegue achar toda letra 'a' msm em minúscula.
print("A primeira aparição da letra A está na posição.", frase.find("A")+1)
#O .find("A") para encontrar o primeiro 'a' e +1 pois começa com 0.
print("A última aparição da letra A está na posição.", frase.rfind("A")+1)
#O .rfind("A") para encontrar o primeiro 'a' da direita (r: right) para esquerda
