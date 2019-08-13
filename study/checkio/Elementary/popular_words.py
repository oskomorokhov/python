#!/usr/bin/env checkio --domain=py run popular-words

# https://py.checkio.org/mission/popular-words/

# In this mission your task is to determine the popularity of certain words in the text.
#
# At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.
#
# When solving this task pay attention to the following points:
#
# The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.The search words are always indicated in the lowercase.If the word wasn’t found even once, it has to be returned in the dictionary with  0 (zero) value.Input:The text and the search words array.
#
# Output:The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.
#
# Precondition:
# The input text will consists of English letters in uppercase and lowercase and whitespaces.
#
#
# END_DESC

import string


def popular_words(text, words):
    text = text.lower()
    l = text.split()
    for i in l:
        l[l.index(i)] = i.strip(string.punctuation)
    c = [l.count(k) for k in words]
    d = dict(zip(words, c))
    return d


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")