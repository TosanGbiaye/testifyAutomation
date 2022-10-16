#  Task 11
# 1. Create a function that accepts two numbers, adds the numbers and prints out the result in the console.
# 2. Create a function that return the string value "Testify Python"
# 3. Invoke/call the two functions



def values(number1 = 3, number2 = 6):
    result = number1 + number2
    print("Result:",result)

values()
values(6)
values(3,8)
values(15,17)

def greet(name):
    print("Name:", name)
    return name
greet("Testify Python")