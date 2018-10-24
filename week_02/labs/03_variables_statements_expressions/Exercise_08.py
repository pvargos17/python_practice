'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''


def converter(var):
    c = var

    F = c * 1.8 + 32

    return f"{c} degrees in celsius = {F} degrees fahrenheit"

temp = 27.4

print(converter(temp))
