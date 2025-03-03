from datetime import date

lista = {'nome': str(input('Digite seu nome: ')),
'nascimento': int(input('Data de nascimento: ')),
'ctps': int(input('Carteira de trabalho (0 nao tem): '))}

lista['nascimento'] = date.today().year - lista['nascimento'] 

if lista['ctps'] != 0:
    lista['contratação'] = int(input('Ano de contratação: '))
    lista['salario'] = float(input('Salário: '))
    lista['aposentadoria'] = (35 - (date.today().year - lista['contratação'])) + lista['nascimento']

print('=-=' * 30)

for n, v in lista.items():
    if n == 'aposentadoria' and date.today().year - lista['aposentadoria'] == 0 and lista['ctps'] != 0:
        print(f'{n} = voçe ja pode aposentar-se')
    else: 
        print(f'{n} = {v}')
