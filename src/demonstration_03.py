"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

we can use the int() constructor to convert other data types to an Integer

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # set my number to the int value of txt
    number = int(txt)
    return number

print(string_int("6"))
print(string_int("1000"))
print(string_int("12"))




