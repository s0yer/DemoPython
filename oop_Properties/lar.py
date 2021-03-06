#exemplo de classe / projeto de classe / blueprint class

class Lar:

    #construtor de lar
    def __init__(self, inicio_area = 0, eletricidade = 0, agua = 0): # construtor de classe, automaticamente é executada quando chamamos a classe
        self.area = inicio_area
        self.eletricidade = eletricidade
        self.agua = agua
        self.__alertas = [] # variavel privada / private variable '__' / so pode ser acessado dentro da classe

    #repr precisa de um retorno
    def __repr__(self):
        print('imprimindo!!')
        return 'area: {}, alertas: {}'.format(self.area, self.__alertas)

    def add_alerta(self, alerta_texto):
        if len(alerta_texto) > 0:
            self.__alertas.append(alerta_texto)
            
    #acessa atributo privado
    def get_alerta(self):
        return self.__alertas

    



