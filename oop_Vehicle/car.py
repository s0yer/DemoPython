# blueprint of the  class
class Car:
    top_speed = 100

    def drive(self):
        print('I am driving in the speed {}'.format(self.top_speed))

# creation of the concrete object

car_purple = Car()
car_purple.drive()