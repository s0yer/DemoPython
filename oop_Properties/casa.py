#exemplo de herança

from oop_properties.lar import Lar

class Casa(Lar):

    #construtor e super para acessar classe pai
    def __init__(self, area = 349, eletricidade = 223, agua = 191):
        super().__init__(area, eletricidade, agua)
        self.__quintal_tamanho = 0

    #metodo esclusivo de casa
    def imposto(self):
        print('o IPTU sera calculado sobre a area de {}'.format(self.area))


def exe_casa():
    # Instanciação
    casa1 = Casa()
    casa2 = Casa(150)

    print(casa1.get_alerta)
    casa1.imposto()
    print(casa1.__dict__)

    print(casa2.get_alerta)
    casa2.imposto()
    print(casa2)
