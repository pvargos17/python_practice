'''
Complete Exercise 10.1 (p.120) from the textbook.

Sum up all elements from a nested list of integers.

'''

t = [[1,2],[3],[4,5,6]]
sum1 = 0

for n in t:
    sum1 += sum(n)
print(sum1)



