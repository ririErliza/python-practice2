
from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['aranti', 'erbay']
anagrams = []

# way 1
# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)


# way 2 using map

# map(function, data)
# newlist = map(aFunction, aData)

print(list(map(jumble,words)))

print([jumble(word) for word in words]) 
#this work the same as above

