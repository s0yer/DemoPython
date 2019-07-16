from lar import Lar

class Casa(Lar):

    
    quintal_tamanho = 0

    def __init__(self, area = 349, eletricidade = 223, agua = 191):
        super().__init__(area, eletricidade, agua)
     
    def imposto(self):
        print('o Imposto sera calculado sobre a area de {}'.format(self.area))

        
# Instanciação
casa1 = Casa()
casa2 = Casa(150)


#casa2.__alertas.append('primeiro alerta')

print(casa1.get_alerta)
casa1.imposto()
print(casa1.__dict__)

print(casa2.get_alerta)
casa2.imposto()
print(casa2)