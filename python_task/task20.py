# Task 20
# 1. Create a class called Human
# 2. Add an attribute leg_count with the value of 4
# 3. Add a method called get_gender() that returns "Unknown" in the Human class
# 4. Create another class called Man that extends Human
# Optionally you can instantiate the classes Man and Woman then print out the values of the get_gender() method in each object instance
class Human:
    leg_count = 4
    def get_gender(self):
        print("Gender: Unknown")

class Man(Human):
    def get_gender(self):
        print("Gender: man")
class Woman(Human):
    def get_gender(self):
        print("Gender: woman")


human = Human()
human.get_gender()

man = Man()
man.get_gender()

woman = Woman()
woman.get_gender()
