todos, tempnota, tempnome = [], [], []
formatacao = '-' * 35
num = 0
while True:
    tempnome.append(str(input('Nome: ').title()))
    tempnota.append(float(input('1° nota: ')))
    tempnota.append(float(input('2° nota: ')))
    todos.append(tempnome[:])
    todos[num].append(tempnota[:])
    tempnome.clear()
    tempnota.clear()
    num += 1
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('{: <7}'.format('num'), end='')
print('{: <15}'.format('NOME'), end='')
print('{: ^7}'.format('MÉDIA'))
print('-' * 29)
for n in range(len(todos)):
    print('{: <7}'.format(n), end='')
    print('{: <15}'.format(todos[n][0]), end='')
    print('{: ^7}'.format((todos[n][1][0] + todos[n][1][1]) / 2))
print(formatacao)
while True:
    no = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if no == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'As notas de {todos[no][0]} sao {todos[no][1]}')
    print('-' * 35)
