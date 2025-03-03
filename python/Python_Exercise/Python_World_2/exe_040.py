n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a media é de {:.1f}'.format(n1, n2, media))
if media <= 4.9:
    print('este aluno foi \033[31mreprovado\033[m')

elif media >= 5.0 and media <= 6.9:
    print('este aluno esta de \033[33mrecuperação\033[m')

else:
    print('este aluno esta \033[32maprovado\033[m')
