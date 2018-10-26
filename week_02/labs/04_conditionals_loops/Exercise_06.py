'''
Using a "while" loop, find the sum of numbers from 1-100.
Print the sum to the console.

'''

# def sumnum(int):
#     sum1 = 0
#     while int > 0:
#         sum1 += num
#         num = num -1
#     print(sum1)
# num = 100
# print(sumnum(num))

count = 0
count_sum = 0

while count <= 100:
    count_sum += count
    count += 1

print(count_sum)
