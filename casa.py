class Casa:
    area = 200

    def imposto(self):
        print('o Imposto sera calculado sobre a area de {}'.format(self.area))

casaA = Casa()
casaA.imposto()