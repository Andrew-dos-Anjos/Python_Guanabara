#Menu de opções
# ----------

n1 = n2 = 0
opcao = 4
while opcao == 4:
    n1 = int(input("¹Número:"))
    n2 = int(input("²Número:"))
    opcao = int(input("[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Recomeçar \n[5]Finalizar\n"))
    if opcao == 1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif opcao == 2:
        print(f"{n1} x {n2} = {n1*n2}")
    elif opcao == 3:
        if n1 == n2:
            print(f"{n1} = {n2}")
        else:
            print(f"{n1} é maior que {n2}") if n1 > n2 else print(f"{n2} é maior que {n1}")
    elif opcao == 5:
        quit()
    else:
        print("\33[31mInvalido!\33[m")
