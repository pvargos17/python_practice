'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''

num1 = int(input("Please give upper bound: "))
num2 = int(input("Please give lower bound: "))

for n in range(num2, num1+1):
    print(n**2)
