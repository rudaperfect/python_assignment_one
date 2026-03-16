# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving")


# Subclass Car
class Car(Vehicle):
    def move(self):
        print("The car is driving")


# Subclass Bike
class Bike(Vehicle):
    def move(self):
        print("The bike is riding")


# Creating objects
v = Vehicle()
c = Car()
b = Bike()

# Calling the method
v.move()
c.move()
b.move()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Question number 2
