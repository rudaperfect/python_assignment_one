class Dog:
    def make_sound(self):
        print("Dog says: Woof!")


class Cat:
    def make_sound(self):
        print("Cat says: Meow!")


def process_sound(sound_object):
    # Calls the make_sound method of the object
    sound_object.make_sound()


# Create objects
dog = Dog()
cat = Cat()

# Pass objects to the function
process_sound(dog)
process_sound(cat)
