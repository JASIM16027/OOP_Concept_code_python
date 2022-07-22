from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("it's running")


class Desktop(Computer):
    def process(self):
        print('Desktop is running ')


com = Laptop()
com.process()
d = Desktop()
d.process()
