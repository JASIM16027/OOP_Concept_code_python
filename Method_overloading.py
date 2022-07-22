# Method overloading


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):

        if a!=None and b!=None and c!=None:
            s = a + b + c

        elif a != None and b != None :
            s = a + b
        else:
            s = a
        return s


stu_1 = Student(40, 80)

print(stu_1.sum(40, 70, 100))
print(stu_1.sum(12, 67))
print(stu_1.sum(34))
