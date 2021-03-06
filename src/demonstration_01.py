"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""
# def addition(a, b):
#     # take two arguments
#     # set a sum to the value of the expression a plus b 
#     sum  = a + b
#     # return our sum to the caller
#     return sum

# this uses one less variable, saves memory
def addition(a, b):
    # take two arguments
    # return our sum to the caller
    # return the value of the expression a plus b 
    return a + b

print(addition(3, 2))
print(addition(-3, -6))
print(addition(7, 3))
