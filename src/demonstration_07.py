"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
def nth_smallest(lst, n):
    # Your code here
    # compare n to the length of the list
    if n > len(lst):
        return None
    # sort list
    new_lst = sorted(lst)

    # find the value at the  n-1 index
    num = new_lst[n-1] # remeber why it is n-1, index starts at 0
        
    # return the nth smallest digit in lst
    return num



print(nth_smallest([7, 5, 3, 1], 1)) # ➞ 1
print(nth_smallest([1, 3, 5, 7], 3)) # ➞ 5
print(nth_smallest([1, 3, 5, 7], 5)) # ➞ None
print(nth_smallest([7, 3, 5, 1], 2)) # ➞ 3  

