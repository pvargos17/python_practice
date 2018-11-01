'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''
fin = open('words.txt')
# print(fin.readline())
for line in fin:
    if len(line) >= 20:
        print(line)
