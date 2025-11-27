def continua(*keep):
    while True:
        k = input("Faça o seu pedido:\n")
        keep += (k,)
        while True:
            repete = input("Quer continuar? [S/N]: ")
            if repete.upper() in ('S', 'N'):
                break
            else:
                print("Por favor, responda com 'S' para Sim ou 'N' para Não.")
        if repete.upper() == 'N':
            break
    return keep


print(f"{'~'*31}\n\033[33m Bem vindo ao Generic-Burguer! \033[m")
keep = continua()
for i, k in enumerate(keep, start=1):
    print(f"Comanda_{i}: {k}")
