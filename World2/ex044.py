#Gerenciador de pagamentos
#----------

loja = str(" Casas baiano ")
print(f"{loja:=^40}")
preco = float(input("Qual é o preço do produto? R$:"))
pag = int(input('''Selecione a seguir o digito referente a forma de pagamento:
[ 1 ] à vista
[ 2 ] cartão
[ 3 ] 2x parcelas
[ 4 ] +3x parcelas\n'''))

if pag == 1:
    print(f"O prod X de R${preco:.2f}, à vista fica R${preco - (preco*10/100):.2f}.")
elif pag == 2:
    print(f"O prod X de R${preco:.2f}, no cartão fica R${preco - (preco*5/100):.2f}.")
elif pag == 3:
    print(f"O prod X de R${preco:.2f}, em 2x parcelas fica R${preco/2:.2f} por parcela.")
elif pag == 4:
    vezes = int(input("Quantas parcelas?:"))
    print(f"O prod X de R${preco:.2f}, em 3x+ parcelas fica R${(preco + (preco*20/100))/vezes:.2f} por parcela.")
else:
    print(f'\033[31mError "{pag}" is an invalid term.\033[m')
