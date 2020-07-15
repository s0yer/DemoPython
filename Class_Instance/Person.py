from random import randint


class Person:

    def __init__(self, initial_age):
        if initial_age < 0 or 1 <= initial_age <= 4:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initial_age

    def amIOld(self):
        if -5 <= self.age <= 30:
            if self.age < 13:
                print("You are young.")
            elif 13 <= self.age < 18:
                print("You are a teenager.")
            elif 18 <= self.age <= 30:
                print("You are old.")
            return self.age
        else:
            return ':)'

    def yearPasses(self):
        if self.age < 30:
            self.age = self.age + 1
            return self.age
        else:
            return self.age


for i in range(0, randint(21, 34)):

    p = Person(randint(-3, 55))
    age_before = p.age
    # ans = 'My age before: {} >>> {}'.format(p.age, p.amIOld())
    # print(ans)
    # print('----------------------------------')
    for j in range(0, 5):
        print(p.yearPasses())
    ans = 'My age before: {} >>> {}'.format(age_before, p.amIOld())
    print(ans)
    print('***********************************')