#Par ou ímpar
#----------

n = int(input("Digite um número:"))
print(f"{n} = ", end="")
if n % 2 == 0:
    print("par")
else:
    print("ímpar")

#A explicação é que N° par /2 equivale a um número inteiro, logo o resto(%) vai ser 0.
'''...para num ímpar == 1, logo...
Também poderia ser feito:

n = int(input("Digite um número:"))
print(f"{n} = ", end="")
if n % 2 == 1:
    print("ímpar")
else:
    print("par")'''
