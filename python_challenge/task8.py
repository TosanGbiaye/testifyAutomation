# Create a program that prints out the even numbers in an array

a = [1, 2, 3, 4, 5, 6]
b = [34, 2, 9, 91, 19, 401, 0]

print("\nEven numbers in a Arrays")
# Using for loop
for num in a:
    if num %2 == 0:
        print(num)

print("\nEven numbers in b Arrays\n")

for num in b:
    if num %2 == 0:
        print(num)