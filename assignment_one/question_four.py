# Dog class
class Dog:
    def make_sound(self):
        print("Woof")


# Cat class
class Cat:
    def make_sound(self):
        print("Meow")


# Function that expects an object with make_sound()
def process_sound(sound_object):
    sound_object.make_sound()


# Creating objects
dog = Dog()
cat = Cat()

# Using the same function for different objects
process_sound(dog)
process_sound(cat)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
