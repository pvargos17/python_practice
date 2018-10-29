'''
Complete Exercise 10.2 (p.120) from the textbook.

'''
t = [1,2,3]
def cumsum(list1):
    total = 0
    new_list=[]
    for i in list1:
        total += i
        new_list.append(total)
    return new_list

print(cumsum(t))
