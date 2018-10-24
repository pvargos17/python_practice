'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

def cost(x,y,z):

    miles = x
    mpg = y
    price = z

    total_cost = (mpg/miles)*price
    return total_cost

print(cost(10,20,5))
