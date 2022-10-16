# Task 25
# 1. Create a class called Utilities
# 2. Create a static method called print_name which accepts a parameter, and prints out the parameter.
# 3. Invoke the static method print_name()
# You can use any of the two methods to create your static methods.
class Utilities:


    def print_name(tissue_paper):
        return tissue_paper

    @staticmethod
    def print_name2(electricity_company):
        return electricity_company

Utilities.print_name = staticmethod(Utilities.print_name)
print("My Tissue paper is : ", Utilities.print_name("Rose_plus"))
print("MY Electricity Company is : ", Utilities.print_name2("Ikeja_dc"))
