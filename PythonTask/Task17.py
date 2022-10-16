# Task 17
# 1. Create a class called Human
# 2. Initialize the class
class Human:
     name = "Man"
     group = "Male"
     def get_name_group(self):
         return self.name + ":" + self.group

Man = Human()
print(Man.name, Man.group, Man.get_name_group())

