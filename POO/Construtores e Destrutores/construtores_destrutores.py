class Cachorro:
    # NOTE: Método construtor
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # NOTE: Método destrutor
    def __del__(self):
        print('Removendo a instância da classe.')

    def falar(self):
        print('auau')

def criar_cachorro():
    cachorro1 = Cachorro('Zeus', 'Branco', False)
    cachorro1.falar()
    print(cachorro1.nome)

    # del cachorro1 # NOTE: Força o destrutor

criar_cachorro()