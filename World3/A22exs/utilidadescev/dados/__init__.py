def leiadinheiro (msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\33[31mERRO: \"{entrada}\" é um preço invalido!\33[m")
        else:
            valido = True
            return float(entrada)
