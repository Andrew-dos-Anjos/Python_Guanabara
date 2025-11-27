#Detector de palíndromo
# ----------

#Resolução simples:
'''frase = input("Digite uma frase:").upper().replace(' ','')
if frase == frase[::-1]:
    print(f'Sua frase:"{frase[::-1]}" é um palíndromo :D')
else:
    print(f'Sua frase não é um palíndromo:"{frase[::-1]}"')'''
#Com os comandos ".replace(' ','')" e "frase[::-1]": ¹Substitui os espaços vazios por nenhum espaço.
#²Inverte a ordem do argumento atribuido.

#Resolução com laço for:
fr = str(input("Digite uma frase:")).strip().upper()
palavras = fr.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Sua frase é um palíndromo B)")
else:
    print("Não é palíndromo.")
#Revisar
