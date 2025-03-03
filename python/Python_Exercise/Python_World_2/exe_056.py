idade = 0
num = 0
media = 0
nwom = 0
iman = 0
nman = 'indefinido'

for c in range(1, 5):
    num = num + 1
    print('{} {}° Pessoa {}'.format('-----', num, '-----'))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ').upper())
    if sexo == 'M':
        if c == 1:
            iman = idade
            nman = nome
        if idade > iman:
            iman = idade
            nman = nome
    elif sexo == 'F':
        if idade <= 20:
            nwom = nwom + 1


media += (idade / 4)
print('''
A media de idade do grupo é de {:.2f} anos
O homem mais velho tem {} anos e se chama {}
ao todo tem {} mulheres com menos de 20 anos'''.format(media, iman, nman, nwom))

