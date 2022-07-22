#Inheritance


class Employee:
    raise_amount = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.'+last+'@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


e1 = Employee("Jasim", "Uddin", 5000)
d1 = Developer("Jasim", "Uddin", 5000, "python")


d2 = Developer("Misbah", "Uddin", 4000, "c++")
d3 = Developer("Jalal", "Uddin", 6000, "Javascript")


mang_1 = Manager("Jasim", "Uddin", 50000, [d1])

print(repr(mang_1))
print(str(mang_1))

#print(int.__add__(1, 5))
#print(str.__add__('hello' + ' '+'world', ' '+'My name is Jasim uddin'))

print(mang_1.email)

mang_1.add_emp(d2)
mang_1.add_emp(d3)
#mang_1.remove_emp(d3)
mang_1.print_emp()
print(isinstance(mang_1, Manager))
print(isinstance(mang_1, Employee))
print()
print()
print(d1.fullname())
print(d1.email)
print(d1.prog_lang)
print(d1.pay)
d1.apply_raise()
print(d1.pay)
print()
print(d2.fullname())
print(d2.email)
print(d2.prog_lang)
print(d2.pay)
d2.apply_raise()
print(d2.pay)


#print(help(Developer))


