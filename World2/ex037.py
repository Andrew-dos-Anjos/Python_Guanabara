#Conversor de bases numéricas
#----------

num = int(input("Digite um número inteiro:"))
opçao = int(input('''Escolha uma das opções de conversão:
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal\n'''))

if opçao == 1:
    print(f"O número {num} em Binário fica:", bin(num)[2:])
elif opçao == 2:
    print(f"O número {num} em Octal fica:", oct(num)[2:])
elif opçao == 3:
    print(f"O número {num} em Hexadecimal fica:", hex(num)[2:])
else:
    print(f'\033[31mError "{opçao}" is an invalid term.\033[m')
