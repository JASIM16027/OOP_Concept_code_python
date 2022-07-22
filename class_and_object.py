class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu, " ", self.ram)


a = 34
print(a.bit_length())

comp1 = Computer("Core i5", "4GB")
comp2 = Computer("Core i7", "8GB")

Computer.config(comp1)
comp1.config()
comp2.config()
comp2.config()
comp2.config()
