class Estudante:
    escola = 'DIO' # Variável de classe

    def __init__(self, nome_estudante, matricula):
        # Variável de instância
        self.nome_estudante = nome_estudante
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome_estudante} - {self.matricula} - {self.escola}'

def mostrar_valores(*objetos):
    for objeto in objetos:
        print(objeto)

aluno1 = Estudante('Guilherme', 1)
aluno2 = Estudante('Giovanna', 2)
mostrar_valores(aluno1, aluno2)

Estudante.escola = 'Python'
aluno3 = Estudante('Choppie', 3)
mostrar_valores(aluno1, aluno2, aluno3)