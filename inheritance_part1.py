class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        print("Don't know how to say ")
    def show(self):
        pass


class Cow(Animal):
    def __init__(self, name, sound, color):
        self.sound = sound
        self.color = color
        super().__init__(name)

    def show(self):
        print(f"Cow name : {self.name}\nSpeak : {self.sound}\nColor : {self.color}")


cow = Cow('Jodu','Hamba', 'Red')
cow.show()