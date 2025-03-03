from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
num = ano % 4

data = date

if ano == 0:
    ano = date.today().year

if num == 0 and ano % 100 != 0 or ano % 400:
    print(f'O ano {ano} é \033[4;33;40mBISSEXTO\033[m')

else:
    print(f'O ano {ano} \033[4;36;40mNÂO É BISSEXTO\033[m')

#erro, configurar e analisar