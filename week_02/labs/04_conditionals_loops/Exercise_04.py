'''
Print out every prime number between 1 and 100.

'''
for n in range(1, 101):
    if n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0 or n % 6 == 0 or n % 7 == 0:
        pass
    else:
        print(n)
