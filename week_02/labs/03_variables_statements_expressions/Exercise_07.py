'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

def future_pop(var):
    # per year
    born = (60*60*24*365)/6
    dies = (60*60*24*365)/12
    immigrates = (60*60*24*365)/40
    current = 380123456

    x = (born * var) + (immigrates * var) - (dies *var)
    return x + current

year = 3

print(future_pop(year))


