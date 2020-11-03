"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""
def mapping(letters):
    # Your code here
    # define a dictionary and initilize it
    letters_dicta = {}

    # iterate thru letters
    for i in range(len(letters)):
        # add to dict[letter[i]] set value to letter[i].upper
        letters_dicta[letters[i]] = letters[i].upper()

    # return dictionary
    return letters_dicta

print(mapping(["p", "s"])) # ➞ { "p": "P", "s": "S" }
print(mapping(["a", "b", "c"])) # ➞ { "a": "A", "b": "B", "c": "C" }
print(mapping(["a", "v", "y", "z"])) # ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }