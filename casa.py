from lar import Lar

class Casa(Lar):
    def __init__(self, area = 50):
        super().__init__(area)
     

        
  
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