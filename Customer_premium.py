class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership = membership_type
        """
    def show(self):
        print(f"Customer name : {self.name}\nMembership_type : {self.membership}")
        """

    def update_membership(self, new_membership):
        self.membership = new_membership

    def __str__(self):
        return self.name + " " + self.membership

    def all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        else:
            return False
    #__hash__ = None
    __repr__ = __str__

# customers = Customer('Md. Jasim Uddin', 'Gold')


customers = [Customer('Md. Jasim Uddin', 'Gold'),
             Customer('Md. Hasan', 'platinum'),
             Customer("Ragib Hasan", 'Bronz')
             ]

print(customers)


"""
print(customers[1])

customers[1].update_membership("platinum")
print(customers[1])

customers[1].update_membership('Gold')
print(customers[0].name)
Customer.all_customers(customers)
print(customers[1] == customers[0])
"""