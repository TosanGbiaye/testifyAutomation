#Using the OOP feature inheritance, create a class Animal with the method sound()
# and then create a Cat and Dog class that inherits from the animal class.
# the Cat and Dog class should override the sound class and print a different sound

class Animal:
    group = "Mammal"
    leg_count = 4
    can_fly = False
    sound = "Unknown"

    def print_sound(self):
        print("\nAnimal Sound: ", self.sound)

class Cat(Animal):
    sound = "meow"
    def __init__(self, sound):
        self.sound = sound

class Dog(Animal):
    sound = "woof"

    def __init__(self, sound):
        self.sound = sound


cat1 = Cat("meow")
cat1.print_sound()
dog1 = Dog("woof")
dog1.print_sound()
