# 22:30
''' Rotina:
a = 1       |a = 3       *|b = 5       |...
b = 2       |b = 4       *|a = 6
c = a + b   |c = a + b   |c = a + b
print(c)    |print(c)    |print(c)
'''


# Função:
def soma(a, b):
    c = a + b
    print(c)


soma(1, 2)
soma(3, 4)
#Também é possível redefinir a ordem dos fatores:
soma(b=5, a=6)


#Função²:
def recebe(* tupla):
    print(tupla)


recebe(1, 2)
recebe(5, 8, 4, 8, 2)
recebe("a", "b", "c")


#Função³:
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
