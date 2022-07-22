class Person:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def speak(self):
        print(f"{self.name} can speak ")

    def walk(self):
        print(f'{self.name} can walk')

    def show(self):
        print(f"Name : {self.name}")
        p.speak()
        print(f"Speaking Language : {self.language}")
        p.walk()


class English_People(Person):
    def speak(self):
        print('Spoken Language: English')

    def country(self):
        print('country : Bangladesh')


p = Person('Jasim Uddin', 25, "Bangla")
p.show()
c = English_People('Jasim Uddin', 25, "Bangla")
c.country()
