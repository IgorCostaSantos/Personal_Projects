dados = {'nome': str(input('Digite seu nome: ').title())}
dados['media'] = float(input(f'Digite a {dados["nome"]}: '))

if dados['media'] < 7.0:
    dados['situacao'] = 'Reprovado'
else:
    dados['situacao'] = 'Aprovado'
print('-=' * 10)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
