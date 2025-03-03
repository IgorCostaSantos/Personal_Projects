from random import randint
jogadores = {}
dados = ''
back = []
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)

print('Valores sorteador:')
for q, y in jogadores.items():
    print(f'o {q} tirou {y}')

for x, c in enumerate(jogadores):
    if x == 0:
        dados = jogadores[c]
    else:
        for p in jogadores.values():
            if dados < p and dados not in back:
                dados = jogadores[c]
        print(f'{x}° lugar: {c} com {p}')
        back = dados
