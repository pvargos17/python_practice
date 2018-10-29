'''
Complete Exercise 10.1 (p.120) from the textbook.

Sum up all elements from a nested list of integers.

'''

t = [[1,2],[3],[4,5,6]]

def nested_func(list1):
    sum1 = 0

    for n in list1:
        sum1 += sum(n)
    return sum1

print(nested_func(t))



