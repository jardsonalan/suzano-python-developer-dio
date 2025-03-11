from datetime import datetime

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # NOTE: Método de classe que cria uma pessoa apartir da data de nascimento
    # NOTE: cls é referência para a classe
    # NOTE: Utilizamos quando precisamos do contexto da classe
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = datetime.now().year - ano
        return cls(nome, idade)
    
    # NOTE: Método estático que verifica se a pessoa é maior de idade
    # NOTE: Utilizamos quando NÃO precisamos do contexto da classe e nem da instância do objeto
    @staticmethod
    def e_maior_de_idade(idade):
        return 'É maior de idade' if idade >= 18 else 'Não é maior de idade'
    
p1 = Pessoa.criar_de_data_nascimento(2005, 4, 4, 'Jardson')
print(p1.nome, p1.idade)

print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(8))