class Person:
    def __init__(self,initialAge):
        if 1 <= t <= 4:
            if initialAge < 0:
                age = 0
                print(" Age is not valid...")
            else:
                age = initialAge
        else:
            print(" t value: [1,4]")

    def amIOld(self):
        if -5 <= age <= 30:
            if age < 13:
                print("You are young.")
            elif 13 <= age < 18:
                print("You are teenager")
            else:
                print("You are old.")

    def yearPasses(self):
        age = age + 1
        return age