e = str(input('Digite a expressão: '))
pilha = []
for c in e:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressao é verdadeira')
else:
    print('A expressao é falsa')



