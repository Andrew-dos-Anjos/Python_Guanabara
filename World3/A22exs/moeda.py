#ex 107
def aumentar(preco, taxa, formato=False):
    '''
    ex 109: __res__ e __formato__;
    Com o 3º param (formato) a escrita como no ex 108
    é substituida com o retorno de True no cod principal.
    '''
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco, taxa, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


#ex 108
def moeda(preco, moeda="R$"):
    return f"{moeda}{preco:.2f}".replace(".", ",")


#ex 110
def resumo(preco, taxaa=10, taxad=20):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço informado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}")
    print(f"{taxad}% de desconto: \t{diminuir(preco, taxad, True)}")
    print("-"*30)


#ex 111: "utilidadescev >> moeda".
#ex 112: "utilidadescev >> dados".
