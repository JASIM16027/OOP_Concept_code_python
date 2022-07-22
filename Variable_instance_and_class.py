class Car:
    wheels = 4            #class variable

    def __init__(self):
        self.com = "BMW"  #instance variable
        self.mil = 20


c1 = Car()
c2 = Car()
c2.com = "Ford"
Car.wheels = 5
#c1.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)