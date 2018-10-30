'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}


new_dict = {}

for c in dict_1:
    new_dict[c] = dict_1[c]
    for d in dict_2:
        new_dict[d] = dict_2[d]
        for e in dict_3:
            new_dict[e] = dict_3[e]
for f in new_dict:
    print(f , new_dict[f])

