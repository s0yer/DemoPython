class Person:

    def __init__(self,initialAge):
        if 1 <= t <= 4:
            if initialAge < 0:
                self.age = 0
                print("Age is not valid, setting age to 0.")
            else:
                self.age = initialAge
        else:
            print(" t value: [1,4]")
        return None

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
            return None

    def yearPasses(self):
        if self.age < 30:
            self.age = self.age + 1
            return self.age
        else:
            return None

t = 4
for i in range(0, t):
    age = 10
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()