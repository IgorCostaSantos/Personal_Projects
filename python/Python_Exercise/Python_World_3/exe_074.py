from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10),)
print('Eu sorteei os valores: ', end='')
for c in num:
       print(f'{c} ', end='')

print(f'''
O maior numero foi {max(num)}
O menor numero foi {min(num)}
''')
