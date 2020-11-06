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
"""

#### Refactor #1
"""
def XO(txt:str) -> bool:
    # set an o anc x counter to zero
    o_counter = 0
    x_counter = 0
    # Loop over each character in the string
    for char in txt:
        # do a check if it contains an "x"
        if char == "x" or char == "X":
            #increment the x counter
            x_counter += 1
        elif char == "o" or char == "O":
            #increment the o counter
            o_counter += 1
    
    # check if x counter is equal to the o counter
    if x_counter == o_counter:
        # return true to the caller
        return True
    # otherwise
    else:
        return False
"""

### Refactor #2

def XO(txt: str) -> bool:
    # lowercase the text
    lower_txt = txt.lower()

    # return the count of lower txt using "o" as a parameter == 
    # the count of lower txt using "x" as a parameter as a boolean value to the caller
    return lower_txt.count("o") == lower_txt.count("x")



print(XO("ooxx")) #➞ True
print(XO("xooxx")) #➞ False
print(XO("ooxXm")) #➞ True (Case insensitive)
print(XO("zpzpzpp")) #➞ True (Returns True if no x and o)
print(XO("zzoo")) #➞ False
