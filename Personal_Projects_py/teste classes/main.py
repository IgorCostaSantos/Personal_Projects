class RemoteControll:
    def __init__(self, cor, altura, profundidade, largura) -> None:
        
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade 
        self.largura = largura
        
    def Passar_Canal(self, botao):
        if botao == '+':
            print('aumentar o canal')
        elif botao == '-':
            print('diminuir o canal')
    #metodo controle remoto
    #   passar canal
    #   aumentar volume
    #   abrir netflix
    #   desligar tv


controle_remoto_1 = RemoteControll('preto' '10cm' '2cm' '2cm') 
controle_remoto_2 = RemoteControll('cinza' '12cm' '5cm' '3cm')
