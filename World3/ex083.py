#Validando expressões matemáticas
# ----------

expressao = str(input("Escreva a expressão matemática: "))
validacao = []
for parenteses in expressao:
    if parenteses == "(":
        validacao.append(1)
    elif parenteses == ")":
        if len(validacao) > 0:
            validacao.pop()
        else:
            print("Expressão invalida!")
            break
if len(validacao) == 0:
    print("Expressão valida!")

#Para a expressão estar correta o N° de "(" e ")" devem ser os mesmos, além de que para cada abertura haja um
#fechamento de maneira que um venha antes do outro e não o contrario.

#Na parte do código, em ordem: Temos a expressão; Validação recebe []; Para cada parenteses(posição) na expressão:;
#Se a posição for == '(' cria um slot de armazenamento em validcao; Se for == ')' e o tamanho de validacao maior que 0,
#significa que há slot(s) preenchidos, sinalizando que tem uma abertura '(' para o fechamento ')', então esse slot é
#deletado(linha 11); Agora se na posição o parenteses for == ')' e não haver nenhuma abertura como pre determinado é
#invalido.