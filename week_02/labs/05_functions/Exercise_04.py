'''
Write a function that takes in a list and finds the max, min, average and sum.

'''
somelist =  [1,12,2,53,23,6,17]

def my_min_function(somelist):
    min_value = None
    for value in somelist:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value
print(my_min_function(somelist))
