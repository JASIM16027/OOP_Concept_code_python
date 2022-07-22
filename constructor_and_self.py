class Computer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = Computer("JASIM UDDIN", 25)
#c1.name = "YASIN"
#c1.age = 28

c2 = Computer(" NAVIN ", 28)

if c1.compare(c2):
    print("they are same age")
else:
    print("Different age")

print(c1.name)
print(c2.name)