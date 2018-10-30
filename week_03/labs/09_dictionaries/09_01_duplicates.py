'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.

Solution: http://thinkpython2.com/code/has_duplicates.py.

Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html

'''


def has_duplicates(list1):
    d = dict()
    for n in list1:
        if n in d:
            return "True"
        else:
            d[n] = 1
    print(d)
x = (1,2,3,4,5,5,6)
y = (1,2,3,4,5,6)

print(has_duplicates(y))
