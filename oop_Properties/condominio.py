#exemplo de classe

from oop_Properties.lar import Lar

class Condominio(Lar):

    #Construtor e super para acessar a classe pai / Constructor and super to access the parent class
    def __init__(self, area = 349, eletricidade = 223, agua = 191):
        #acessa dados da classe filha
        super().__init__(area, eletricidade, agua)
    #metodo exclusivo de condominio
    def mensalidade(self):
        mensalidade_total = self.eletricidade + self.agua + self.area * 1.09
        return mensalidade_total

def exe_condominio():
    cond1 = Condominio()
    cond2 = Condominio(100,200,300)

    print(cond1.mensalidade())
    print(cond1.get_alerta)
    print(cond2.mensalidade())
    print(cond2.get_alerta)
