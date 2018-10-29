'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''
def make_tuple(list1):
    new_tuple = []
    x = list1.sort()
    for i in x:

