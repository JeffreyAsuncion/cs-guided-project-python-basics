"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # count number of x and o's
    # compare if num_x == num_0
    txt = txt.lower()
    num_x = 0
    for letter in txt:
        if letter == "x":
            num_x += 1
    
    num_o = 0
    for letter in txt:
        if letter == "o":
            num_o += 1

    if num_x == num_o:
        return True
    else:
        return False

print(XO("ooxx")) #➞ True
print(XO("xooxx")) #➞ False
print(XO("ooxXm")) #➞ True (Case insensitive)
print(XO("zpzpzpp")) #➞ True (Returns True if no x and o)
print(XO("zzoo")) #➞ False
