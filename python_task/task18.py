# Task 18
# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add another attribute can_walk with value of True
# Optionally you can instantiate the class and prints out the leg_count and can_walk attributes
class Human:
    leg_count = 4
    can_walk = True
    def __init__(self, name):
        self.name = name

man = Human("man")
woman = Human("woman")

print(man.leg_count)
print(woman.leg_count)

print(man.can_walk)
print(woman.can_walk)
