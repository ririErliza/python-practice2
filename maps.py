# map(function, data)
# newlist = map(aFunction, aData)


from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)

words = ['beetrot', 'carrots', 'potatoes']
anagrams = []