from abc import ABC, abstractmethod

# NOTE: Classes Abstratas não podem ser instanciadas diretamente
class ControleRemoto(ABC):
    # NOTE: @abstractmethod - obriga as classes filhas a implementar os métodos
    @abstractmethod
    def ligar(self):
        pass
    
    # NOTE: @abstractmethod - obriga as classes filhas a implementar os métodos
    @abstractmethod
    def desligar(self):
        pass
    
    # NOTE: Propriedade abstrata
    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando: TV')

    def desligar(self):
        print('Desligando: TV')

    @property
    def marca(self):
        return 'Philco'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando: Ar Condicionado')

    def desligar(self):
        print('Desligando: Ar Condicionado')
    
    @property
    def marca(self):
        return 'LG'

controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
print(controle_tv.marca)

controle_ar_condicionado = ControleArCondicionado()
controle_ar_condicionado.ligar()
controle_ar_condicionado.desligar()
print(controle_ar_condicionado.marca)