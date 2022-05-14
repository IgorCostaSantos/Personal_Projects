class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']

        if plano in self.lista_planos:
            self.plano = plano

        else:
            raise Exception('\033[31mPlano invalido\033[m')

    def mudar_plano(self, novo_plano):

        if novo_plano in self.lista_planos:
            self.plano = novo_plano

        else:
            print('\033[31mPlano Invalido\033[m')

    def ver_filme(self, filme, plano_filme):

        if self.plano == plano_filme:
            print(f'ver filme {filme}')

        elif self.plano == 'premium':
            print(f'ver filme {filme}')

        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faca upgrade para premium, para ver filme')

        else:
            print('plano invalido')

        self.filme = filme
        self.plano_filme = plano_filme


Cliente = Cliente('Igor', 'igor@gmail.com', 'basic')
print(Cliente.plano)
Cliente.ver_filme('Harry Potter', 'premium')

Cliente.mudar_plano('premium')
print(Cliente.plano)
Cliente.ver_filme('Harry Potter', 'premium')
