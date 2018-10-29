'''
Complete Exercise 10.7 (p.121) - the birthday paradox - from the textbook.

'''
t = [1,2,3,4,4,5,6]
v = [1,2,3,4,5,6,7]

def has_duplicates(list1):
    new_list = []
    for n in list1:
        if n in new_list:
            return "True"
        else:
            new_list.append(n)
print(has_duplicates(t))
