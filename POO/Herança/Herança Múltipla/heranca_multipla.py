class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

# NOTE: (**kw) Resolve o erro de parâmetros iguais em duas (ou mais) classes
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)

        # NOTE: Apresenta a ordem de resolução da classe
        print(Ornitorrinco.__mro__)

gato = Gato(numero_patas=4, cor_pelo='Preto')
print(gato)

ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo='Verde', cor_bico='Laranja')
print(ornitorrinco)