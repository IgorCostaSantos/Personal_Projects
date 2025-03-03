id = idm = idf = 0

while True:
    print('---' * 7)
    print('   CADASTRE UMA PESSOA   ')
    print('---' * 7)
    year = int(input('Quantos anos a pessoa tem: '))
    while True:
        sexo = str(input('Qual o sexo dessa pessoa: (M/F) ')).upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
    print('---' * 7)
    if sexo == 'M':
        idm += 1
    if sexo == 'F' and year < 20:
        idf += 1
    if year > 18:
        id += 1
    while True:
        rep = str(input('Voce quer continuar? [S/N] ')).upper()
        if rep == 'S' or rep == 'N':
            break
    if rep == 'N':
        break

print('---' * 7)
print('  FIM DO PROGRAMA  ')
print('---' * 7)

print(f'''
{id} Pessoas tem mais de 18 anos
{idm} Homens foram cadastrados
{idf} Mulheres tem menos de 20 anos
''')
