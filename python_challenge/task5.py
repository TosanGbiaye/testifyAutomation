# Write a python program that checks if a string is a palindrome.
# Then optionally write a unit test to check your program's correctness
# PS: A palindrome Python program is used to check whether a string is the same from forward to backward.

str1 = input("Enter the string to check if it is a palindrome: ")
str1 = str1.casefold()
rev_str = reversed(str1)
if list (str1) == list(rev_str):
    print("The string is a palindrome")

else:
    print("The string is not a pallindrome")

#Alternatively
# Use String Indexing in Python to check if a String is a Palindrome
print("\nMethod2")

a_string = 'Was it a car or a cat I saw'

def palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    return a_string == a_string[::-1]

print(palindrome(a_string))