
#instance,class and static method


class Student:
    university ="MBSTU" # static variable or class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getAvg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod        #decorator
    def info(cls):
        return cls.university

    def setM(self, value1, value2, value3):
        self.m1 = value1
        self.m2 = value2
        self.m3 = value3

    def getM(self):
        return self.m1, self.m2, self.m3


c1 = Student(90, 80, 75)
print(c1.getAvg(), Student.info())

c1.setM(10, 20, 40)
print(c1.getAvg(), Student.info())




