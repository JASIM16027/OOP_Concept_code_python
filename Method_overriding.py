class Father:
    def show(self):
        print("Land")


class Myself(Father):

    def show(self):
        print("I have a beautiful garden")


my = Myself()
my.show()