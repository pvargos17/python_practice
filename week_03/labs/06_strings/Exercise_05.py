'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

# def problem(str)

user_str = input("Please enter something you asshat: ")

capital = " "
lower = " "
vowel = "aeiou"
vowels = " "

for n in user_str:
    if n.isupper():
        capital += n
    if n.islower():
        lower+= n
    if n in vowel:
        vowels +=n
print(capital)
print(lower)
print(vowels)

