'''
Complete exercises in section 8.7 (p.75)

CODE:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

1) - Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter as arguments.

2) - Rewrite this function so that instead of traversing the string,
it uses the three-parameter version of find from the previous section.

'''
def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count_again(word, letter):
    index, count = 0, 0
    for i in range(len(word)):
        index = find(word, letter, index)
        if index == -1:  # if no match is found, break the loop
            break
        else:  # otherwise increment both
            count += 1
            index += 1  # becomes the new starting point for find()
    return count
