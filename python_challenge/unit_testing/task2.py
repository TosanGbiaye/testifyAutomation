# create a function that calculates the power of a number .
# Then write a unit test to check the correctness of the function

"""
import math
print(math.pow(4,2))

"""
# n is number, e is exponent , res = result
"""
def power(n,e):
    res=0
    for i in range(e):
        res *= n
    return res
print(pow(4,2))
"""
def power(a, b):
    return a ** b

