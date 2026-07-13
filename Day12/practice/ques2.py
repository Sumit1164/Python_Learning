class Animals():
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    # First Method
    @staticmethod
    def bark():
        print("Bow Bow!")

    # Second Method
    def bark(self):
        print("Bow Bow!")


d = Dog()
d.bark()