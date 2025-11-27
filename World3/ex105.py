#Analisando e gerando Dicionários
# ----------

def notas(*n, sit=False):
    '''
    —> Função para analisar notas e situações de vários alunos.
    param n: uma ou mais notas dos alunos (aceita várias)
    param sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma.
    '''
    dic = dict()
    dic["Total"] = len(n)
    dic["Menor"] = min(n)
    dic["Maior"] = max(n)
    dic["Média"] = sum(n)/len(n)
    if dic["Média"] < 5:
        dic["Situação"] = "Ruim"
    elif dic["Média"] >= 7:
        dic["Situação"] = "Boa"
    else:
        dic["Situação"] = "Razoável"
    return dic


resp = notas(7, 3.5, 10, sit=True)
print(resp)
help(notas)
