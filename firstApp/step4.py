import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def movie(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.draw()
point1.movie()

point2 = Point(10, 12)
print(point2.x)


# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()

# Modules
# import converters
# from converters import kg_to_lbs

# import package
# import ecomerce.shipping
# from ecomerce.shipping  import calculate_shipping
# from ecommerce import shipping


# Generating Random values
for i in range(3):
    print(random.random())
    