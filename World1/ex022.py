#Analisador de textos
#----------

nome = str(input("Diga seu nome todo:")).strip()

print("Seu nome em caps lock: ", nome.upper())
print("Seu nome em caps_lockn't: ", nome.lower())

space = nome.count(" ")
print(f"Seu nome tem {len(nome)-space} atributos.")
x = nome.find(" ")
print(f"Seu primeiro nome é {nome.split()[0]} e tem {x} atributos.")

#A var "x" identifica o n° de caracteres até o primeiro espaço, sendo o primeiro = 0,
#o espaço contribui na contagem fazendo com que essa diferença seja reparada.
