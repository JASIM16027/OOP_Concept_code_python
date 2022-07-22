class Student:   #outer class
    def __init__(self, name, rollno):
        self.s_name = name
        self.s_roll = rollno
        self.lap = self.Laptop("HP", "I5", "4GB")

    def show(self):
        print(self.s_name, self.s_roll)
        self.lap.show()

    class Laptop: # inner class
        def __init__(self, brand, cpu, ram ):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Jasim Uddin", 16027)
s2 = Student("Misbah Uddin", 16019)
s1.show()
s2.show()
#s2.lap.show()