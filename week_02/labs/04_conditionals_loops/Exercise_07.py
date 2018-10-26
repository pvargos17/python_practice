'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''

count = 1000
iterration = 1
while count >= 1:
    if iterration == 3:
        print(count)
        iterration = 1
    else:
        iterration +=1
    count = count - 1


