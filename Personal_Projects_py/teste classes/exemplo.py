class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.lista_planos = ["basic", "premium"]
        if plano not in self.lista_planos:
            raise Exception('plano invalido')
        
    def mudar_plano(self, NovoPlano):
        if NovoPlano in self.lista_planos:
            self.plano = NovoPlano
        else:
            print('Plano invalido')
        
    def ver_filmes(self, filme, serie):


Cliente = Cliente('Igor', 'email.gmail.com', 'basic')
print(cliente.plano)

#no update
cliente.mudar_plano = 'premium'
print(cliente.plano)

