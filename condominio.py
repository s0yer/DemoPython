from lar import Lar

class Condominio(Lar):

    def __init__(self, area = 349, eletricidade = 223, agua = 191):
        super().__init__(area, eletricidade, agua)

    def mensalidade(self):
        mensalidade_total = self.eletricidade + self.agua + self.area * 1.09
        return mensalidade_total

cond1 = Condominio()
cond2 = Condominio(100,200,300)

print(cond1.mensalidade())
print(cond1.get_alerta)
print(cond2.mensalidade())
print(cond2.get_alerta)
