tup = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
       'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in tup:
    print(f'\nNa palavra {p} temos ', end='')
    for l in p:
        if l in 'AEIOU':
            print(l.lower(), end=' ')
''