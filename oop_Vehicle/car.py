# blueprint class
# encapsulation -> private and public
class Car:
    #class atribute (dont use atributes here, bad behavior)
    top_speed = 100
    warnings = []

    #special metod, define atributes, converges to desired behavior
    def __init__(self, start_speed = 55):
        #public atributes
        self.top_speed_init = start_speed
        self.observations = []
        #private atribute
        self.__secret_observations = []
        self.trunk_size = 5

    # return de output / return -> need to be a string
    def __repr__(self):
        print('Special Methods!!!')
        return 'Speed: {}, Observations:{}'.format(self.top_speed_init,len(self.observations))

    # private method to add obs in the list -> __secret_observations
    def add_secret_observation(self, observation_text):
        if len(observation_text) > 0:
            self.__secret_observations.append(observation_text)

    # to access the value in secret_observations<private>
    def get_observations(self):
        return self.__secret_observations
    #function access directly the class
    def drive(self):
        print('I am driving in the speed {}'.format(self.top_speed))

    #function that change the atribute instantiated
    def drive_init(self):
        print('I am driving in the speed {}'.format(self.top_speed_init))

    def get_trunk_size(self):
        print('The size of the trunk of this vehicle is {}'.format(self.trunk_size))

def unwanted_behavior():
    print('Unwanted Behavior:')

    # creation of the concrete object
    car_purple = Car()
    car_purple.drive()

    # you can change class atributes, unwanted behavior
    Car.top_speed = 200
    car_purple.warnings.append('warning change')

    car_blue = Car()
    car_blue.drive()
    print(car_blue.warnings)

    car_pink = Car()
    car_pink.drive()
    print(car_pink.warnings)

    print('-------------------------------------------------------------')

    return 0


   # you dont change class atributes of the other instances
def desired_behavior():
    # creation of the concrete object
    print('Desired Behavior:')

    car_yellow = Car()
    car_yellow.drive_init()

    car_yellow.observations.append('observation of change')

    car_red = Car(89)
    car_red.drive_init()
    print(car_red.observations)

    car_blaze = Car(144)
    car_blaze.drive_init()
    print(car_blaze.observations)

    print('-------------------------------------------------------------')

    return 1

def special_methods():

    car_green = Car()

    #Address object in memory
    print(car_green)
    #Object as a dictionary
    print(car_green.__dict__)

    print('-------------------------------------------------------------')

    return 2

def private_method():

    car_black = Car()
    car_black.add_secret_observation('The way to do it is to be.')
    print(car_black.get_observations())
    print('-------------------------------------------------------------')

    return 3

def public_method():

    car_orange = Car()
    car_orange.trunk_size = 8
    car_orange.get_trunk_size()
    print('-------------------------------------------------------------')

    return 4

desired_behavior()
unwanted_behavior()
special_methods()
private_method()
public_method()