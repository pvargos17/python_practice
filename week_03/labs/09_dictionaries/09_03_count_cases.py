'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''


def count_sent(str1):
    counter = {"Upper case": 0, "Lower case" : 0, "Punctuation" : 0}
    for i in str1:
        if i.isupper():
            counter["Upper case"] += 1
        elif i.islower():
            counter["Lower case"] += 1
        elif i == "." or i == "!" or i == "?" or i == ",":
            counter["Punctuation"] += 1
    for p in counter:
        print(p , counter[p])
    return len(str1)
x = "I love to work with dictionaries!"
print(count_sent(x))
