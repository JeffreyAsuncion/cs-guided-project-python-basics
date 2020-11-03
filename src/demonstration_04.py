"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""

def find_perimeter(length, width):

    # Your code here
    # to get the perimeter of a rectangle we could use either (l * 2 + w * 2) or (l + w) * 2
    # return the value of the expression 2* length + 2 * width
    return 2 * length + 2 * width


print(find_perimeter(6, 7)) # 26
print(find_perimeter(20, 10)) # 60
print(find_perimeter(2, 9))  # 22


