from vehicle import Vehicle

class Bus(Vehicle):

    def __init__(self,start_speed=34):
        # public atributes
        self.top_speed_init = start_speed
        self.observations = []
        # private atribute
        self.__secret_observations = []
        self.trunk_size = 5
        #atribute Bus
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)

bus_candy = Bus(55)
bus_candy.add_group([Jadson, Tania, Alberta, Helios])
print(bus_candy.passengers)
