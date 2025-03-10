class Foo:
    def __init__(self, x=None):
        self.__x = x

    # NOTE: Atributo gerenciado para retornar o valor de x
    @property
    def x(self):
        return self.__x or 0
    
    # NOTE: Atributo gerenciado para fazer uma atribuição a x
    @x.setter
    def x(self, valor):
        self.__x += valor

    # NOTE: Atributo gerenciado para ser utilizado quando não queremos excluir um atributo da memória
    @x.deleter
    def x(self):
        self.__x = 0
    
foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)