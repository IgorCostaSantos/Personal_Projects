altura = float(input('Qual a sua altura atual: (M)'))
peso = float(input('Qual o seu peso atual: (KG)'))
IMC = peso / (altura ** 2)
cores = {
'vermelho' : '\033[31m',
'verde' : '\033[32m',
'amarelo' : '\033[33m',
'azul' : '\033[34m',
'roxo' : '\033[35m',
'ciano' : '\033[36m',
'preto_e_branco' : '\033[7,37m',
'limpo' : '\033[m',
}
print('{}seu IMC é de {:.2f}.{}'.format(cores['ciano'], IMC, cores['limpo']))
if IMC < 18.5:
    print('{}voce esta ABAIXO DO PESO ideal.{}'.format(cores['amarelo'], cores['limpo']))
elif IMC < 25:
    print('{}Voce esta no PESO IDEAL.{}'.format(cores['verde'], cores['limpo']))
elif IMC < 30:
    print('{}Voce esta com SOBREPESO.{}'.format(cores['preto_e_branco'], cores['limpo']))
elif IMC < 40:
    print('{}Voce esta com OBESIDADE.{}'.format(cores['roxo'], cores['limpo']))
else:
    print('{}Voce esta com OBESIDADE MORBIDA.{}'.format(cores['vermelho'], cores['limpo']))



