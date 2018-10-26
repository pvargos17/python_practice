'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''

num1 = int(input("Please give an upperbound: "))
num2 = int(input("Please give a lowerbound: "))

sum1 = 0

for n in range(num2, num1 + 1):
    sum1 += n

average = (num1 + num2)/2

print(sum1)
print(average)
