#Primeiro e último nome
#----------

nome = str(input("Diga seu nome completo:")).strip()
first = nome.split()
#Essa variável separa cada palavra fornecida pelos espaços vazios.
print(f"Olá, seu primeiro nome é {first[0]} e o último {first[len(first)-1]}")
#O 1°{} evidencia a primeira <str>
#O 2°{} faz com que a última <str> seja mostrada ao adicionar -1.
