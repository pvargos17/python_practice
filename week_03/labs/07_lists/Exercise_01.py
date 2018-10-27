'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''
user_input = input("Please enter 10 numbers: ").split()
numbers = [float(num) for num in user_input]

# calculating the sum of all numbers
num_sum = 0
for num in numbers:
    num_sum += num
print(num_sum)

avg = sum(numbers) / len(numbers)
print(avg)
