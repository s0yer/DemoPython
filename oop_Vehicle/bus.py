from vehicle import Vehicle

class Bus(Vehicle):

    def __init__(self, start_speed=34):
        # access to child class attributes
        super().__init__(start_speed)
        # atribute Bus
        self.passengers = []

    # method class Bus
    def add_group(self, passengers):
        self.passengers.extend(passengers)

def exe_bus():
    bus_candy = Bus(55)

    print('-----------------------------------')
    bus_candy.add_group(['Jadson, Tania, Alberta, Helios'])
    print(bus_candy.passengers)
    print('-----------------------------------')
    bus_candy.add_secret_observation('When two armies of equivalent strength are confronted, the one who suffers from sustaining the war will achieve victory.')
    print(bus_candy)
    print('-----------------------------------')
