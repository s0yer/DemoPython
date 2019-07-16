class Lar:

    def __init__(self, inicio_area = 200): # construtor de classe, automaticamente é executada quando chamamos a classe
        self.area = inicio_area
        self.__alertas = [] # variavel privada / private variable '__' / so pode ser acessado dentro da classe

    def __repr__(self):
        print('imprimindo!!')
        return 'area: {}, alertas: {}'.format(self.area, self.__alertas)

    def add_alerta(self, alerta_texto):
        if len(alerta_texto) > 0:
            self.__alertas.append(alerta_texto)

    def get_alerta(self):
        return self.__alertas

    def imposto(self):
        print('o Imposto sera calculado sobre a area de {}'.format(self.area))




