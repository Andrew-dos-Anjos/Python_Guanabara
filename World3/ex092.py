#Cadastro de Trabalhador em Python
# ----------

from datetime import datetime

dicionario = {'Nome': str(input("Informe o nome:")),
              'Nascimento': int(input("Informe o ano de nascimento:")),
              'CTPS': int(input("Informe a carteira de trabalho (0 se não tiver):"))}
dicionario['Idade'] = datetime.now().year - dicionario['Nascimento']
if dicionario['CTPS'] != 0:
    dicionario['Contratação'] = int(input("Informe o ano de contratação:"))
    dicionario['Salário'] = float(input("Informe o salário: R$"))
    dicionario['Aposentadoria'] = dicionario['Idade'] + ((dicionario['Contratação'] + 35) - datetime.now().year)
print("-="*20)
for k, v in dicionario.items():
    print(f"  - {k} tem valor ({v})")
