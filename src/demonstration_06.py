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

    # convert txt to lowercase with .lower()
    txt = txt.lower()

    # initialize num_x = 0
    num_x = 0

    # for each letter in txt
    for letter in txt:
        # check if it is an "x"
        if letter == "x":
            # add to num_x the x counter
            num_x += 1
    
    # for each letter in txt
    num_o = 0
    for letter in txt:
        # check if it is an "o"
        if letter == "o":
            # add to num_o the o counter
            num_o += 1

    # check it  num_x and num_o are same
    if num_x == num_o:
        # return they are the same 
        return True
    else:
        # return they are different
        return False

print(XO("ooxx")) #➞ True
print(XO("xooxx")) #➞ False
print(XO("ooxXm")) #➞ True (Case insensitive)
print(XO("zpzpzpp")) #➞ True (Returns True if no x and o)
print(XO("zzoo")) #➞ False
