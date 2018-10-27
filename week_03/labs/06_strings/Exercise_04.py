'''
Write a script that finds the first vowel in a a user inputted string.

'''
def vowel(string):

    vowels = "aeiou"

    for s in string:
        if s in vowels:
            return print(s)
            break

print(vowel("ball"))
