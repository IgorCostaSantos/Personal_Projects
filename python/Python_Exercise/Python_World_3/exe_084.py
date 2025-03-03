
val = []
val2 = []
numc = nump = numl = 0

while True:
    val2.append(str(input('digite o seu nome: ')))
    val2.append(float(input('digite o seu peso: ')))
    numc += 1
    if val2[1] > 100:
        nump += 1
    else:
        numl += 1
    val = val2[:]
    val2.clear()
    r = str(input('Voce quer continuar? [S/N] ')).upper()
    if r == 'N':
        break
print(f'''A quantidade de pessoas cadastradas é de {numc}.''')
print(f'tem {nump} pessoas com o peso acima de 100KG', end=' ')
for p in range(1, len(val), 2):
    if p > 100:
        print(p, end='')

print(f'e {numl} pessoas com menos de 70KG', end='')
for x in range((1, len(val), 2)):
    if x < 70:
        print(x, end='')
