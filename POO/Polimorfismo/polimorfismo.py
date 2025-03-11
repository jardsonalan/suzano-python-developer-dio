class Passaro:
    def voar(self):
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar')

# FIXME: Exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print('Decolando...')

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())