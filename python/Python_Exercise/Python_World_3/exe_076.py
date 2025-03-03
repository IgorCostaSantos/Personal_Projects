t = ('Lápis', 1.75, 'Borracha', 2.00,
     'Caderno', 15.90, 'Estojo', 25.00,
     'Transferidor', 4.20, 'Compasso', 9.99,
     'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f'___' * 10)
print('{: ^30}'.format('LISTAGEM DE PREÇOS'))
print(f'___' * 10)
for c in range(0, 18, 2):
     print('{:.<30}R${: >7 }'.format(t[c], t[c+1]))





