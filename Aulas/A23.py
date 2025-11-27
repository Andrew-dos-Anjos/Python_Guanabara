#18:30
try:
    teste = int(input("Digite um número para validar ou uma letra para causar uma falha... "))

except:
    print("Ocorreu uma falha! \nBad ending :(")

else:
    print(f"Número digitado: {teste} \nGood ending :)")

finally:
    print("Mensagem de encerramento!")


try:
    valor = int("um")    # Isso vai causar um ValueError
    tipo = str(1)        # Isso vai causar um TypeError
    zero = 1 / 0         # Isso vai causar um ZeroDivisionError
    chave = {}["chave"]  # Isso vai causar um KeyError

except (ValueError, TypeError):
    print("Problemas com os tipos de dados.")
except ZeroDivisionError:
    print("O programa levou a uma divizão por 0.")
except KeyError:
    print("Falta de dados nas informações fornecidas.")
except Exception as erro:
    print("Para qualquer outro tipo de erro:", erro.__cause__)
