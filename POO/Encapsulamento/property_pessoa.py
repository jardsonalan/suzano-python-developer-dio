from datetime import datetime

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento

    # NOTE: Atributo gerenciado para retornar o nome
    @property
    def nome(self):
        return f'Nome: {self.__nome}'
    
    # NOTE: Atributo gerenciado para retornar a idade da pessoa
    @property
    def idade(self):
        __ano_atual = datetime.now().year
        return f'Idade: {__ano_atual - self.__ano_nascimento}'
    
pessoa = Pessoa('Jardson', 2005)
print(pessoa.nome)
print(pessoa.idade)