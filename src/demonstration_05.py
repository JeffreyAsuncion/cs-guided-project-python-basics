"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    # how to sort a list in python sort() vs sorted()
    # .sort() modifies list in-place
    # we will use sort with the key attribute set to len 
    lst.sort(key=len)
    return lst

print(sort_by_length(["a", "ccc", "dddd", "bb"])) # ➞ ["a", "bb", "ccc", "dddd"]
print(sort_by_length(["apple", "pie", "shortcake"])) # ➞ ["pie", "apple", "shortcake"]
print(sort_by_length(["may", "april", "september", "august"])) # ➞ ["may", "april", "august", "september"]
print(sort_by_length([]))