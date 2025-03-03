times = ('Atletico Mineiro', 'Flamengo', 'Palmeiras',
         'Fortaleza', 'Corinthians', 'Bragantino SP',
         'Fluminense', 'America FC MG', 'Goianiense GO',
         'Santos', 'Ceara', 'Internacional', 'Sao Paulo',
         'Paranaense', 'Cuiaba', 'Juventude', 'Gremio', 'Bahia', 'Recife', 'Chapecoense')

print('-=-' * 10)
print(f'Liata de times do brasileirão: {times}')
print('-=-' * 10)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=-' * 10)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-=-' * 10)
print(f'Times na ordem alfabetica: {sorted(times)}')
print('-=-' * 10)
print(f'Chapecoense esta na {times.index("Chapecoense")+1} posição')
print('-=-' * 10)
