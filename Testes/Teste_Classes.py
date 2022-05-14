class RemoteControl:
    def __init__(self, color, altura, profundidade, largura):
        self.color = color
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')



remote_control = RemoteControl('preto', '10cm', '2cm', '2cm')
print(remote_control.altura)

remote_control.passar_canal('+')

remote_control2 = RemoteControl('Cinza', '10cm', '2cm', '2cm')
print(remote_control2.color)
remote_control2.passar_canal('-')



