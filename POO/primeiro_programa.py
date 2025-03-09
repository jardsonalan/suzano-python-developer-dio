class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print('Bicicleta parada!')

    def correr(self):
        print('Vruumm...')
    
    # NOTE: Exibe o nome da classe e seus atributos
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

bicicleta1 = Bicicleta('Vermelha', 'Caloi', 2022, 600)
bicicleta1.buzinar()
bicicleta1.parar()
bicicleta1.correr()
print(bicicleta1.cor, bicicleta1.modelo, bicicleta1.ano, bicicleta1.valor)

bicicleta2 = Bicicleta('Verde', 'Monark', 2000, 189)
print(bicicleta2)
bicicleta2.correr()