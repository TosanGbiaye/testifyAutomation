# write a function that removes repeated characters from a string
# sample strings are: 1). Hello   2). Concatenate

"""
from collections import OrderedDict
string1 = "Hello"
string1.lower()
print("".join(OrderedDict.fromkeys(string1)))
"""

from collections import OrderedDict
def remove_duplicates(value):
        m=list(OrderedDict.fromkeys(value))
        s=''
        for i in m:
            s+=i
        return s
print(remove_duplicates("Hello"))
print(remove_duplicates("Concatenate"))



