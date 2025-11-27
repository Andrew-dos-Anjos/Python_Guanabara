#Área quadrada
#Meça a área de uma parede pela altura x largura e calcule quanta tinta é necessário para pintala (1L/2m²)
#----------

al = float(input("Informe o tamanho em metros da altura:"))
la = float(input("Informe o tamanho em metros da largura:"))
area = al*la
tinta = area*0.5
#Ou area/2
print(f"São necessários {tinta}L para pintar a parede, que possui {area}m².")
