from datetime import date
atual = date.today().year
data = int(input('Digite o ano de seu nascimento: '))
idade = atual - data

cores = {
'vermelho' : '\033[31m',
'verde' : '\033[32m',
'roxo' : '\033[35m',
'limpo' : '\033[m'}

print("""
    Quem nasceu em {} tem {} anos em {}.""".format(data, idade, atual))
if data > atual - 18:
    faltam = (data + 18) - atual
    print("""
    Ainda falta {} anos para o alistamento
    {}Seu alistamento sera em {}.{}"""
          .format(faltam, cores['verde'], faltam + atual, cores['limpo']))

elif data < atual - 18:
    devia = atual - (data + 18)
    print("""
    voce ja deveria ter se alistado a {} anos.
    {}Seu alistamento foi em {}.{}"""
    .format(devia, cores['vermelho'], atual - devia, cores['limpo']))

else:
    print("""
    {}Voce deve se alistar IMEDIATAMENTE!!!{}""".format(cores['roxo'], cores['limpo']))
