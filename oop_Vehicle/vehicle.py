
class Vehicle():

    # class atribute (dont use atributes here, bad behavior)
    top_speed = 100
    warnings = []

    # special metod, define atributes, converges to desired behavior
    def __init__(self, start_speed=34):
        # public atributes
        self.top_speed_init = start_speed
        self.observations = []
        # private atribute
        self.__secret_observations = []

    # return de output / return -> need to be a source_text
    def __repr__(self):
        print('Special Methods!!!')
        return 'Speed: {}, Observations:{}, Secret Observations: {}'.format(self.top_speed_init, len(self.observations),len(self.__secret_observations))

    # private method to add obs in the arr -> __secret_observations
    def add_secret_observation(self, observation_text):
        if len(observation_text) > 0:
            self.__secret_observations.append(observation_text)

    # to access the value in secret_observations<private>
    def get_observations(self):
        return self.__secret_observations

    # function access directly the class
    def drive(self):
        print('I am driving in the speed {}'.format(self.top_speed))

    # function that change the atribute instantiated
    def drive_init(self):
        print('I am driving in the speed {}'.format(self.top_speed_init))