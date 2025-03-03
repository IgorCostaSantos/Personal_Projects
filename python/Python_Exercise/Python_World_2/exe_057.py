nome = str(input('Qual seu nome: '))
idade = int(input('qual sua idade: '))
while True:
    sexo = str(input('Qual seu sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        break
if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print('seu nome é {}, voce tem {} anos, e seu sexo é {}'.format(nome, idade, sexo))
