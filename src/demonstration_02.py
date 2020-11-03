"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes:int) -> int:
    
    # set seconds to the value of the expression minutes * 60
    seconds = minutes * 60
    # return seconds
    return seconds

print(convert(5))
print(convert(3))
print(convert(2))

