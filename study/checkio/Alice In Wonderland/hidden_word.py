#!/usr/bin/env checkio --domain=py run hidden-word

# https://py.checkio.org/mission/hidden-word/

# .story img {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/    }JABBERWOCKY'Twas brillig, and the slithy toves
# Did gyre and gimble in the wabe;
# All mimsy were the borogoves,
# And the mome raths outgrabe.
#
# 'Beware the Jabberwock, my son!
# The jaws that bite, the claws that catch!
# Beware the Jubjub bird, and shun
# The frumious Bandersnatch!'
#
# He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
#
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!
#
# One, two! One, two! And through and through
# The vorpal blade went snicker-snack!
# He left it dead, and with its head
# He went galumphing back.
#
# 'And hast thou slain the Jabberwock?
# Come to my arms, my beamish boy!
# O frabjous day! Callooh! Callay!'
# He chortled in his joy.
#
# 'Twas brillig, and the slithy toves
# Did gyre and gimble in the wabe;
# All mimsy were the borogoves,
# And the mome raths outgrabe.
#
# "Through the Looking-Glass." Lewis Carroll
#
# DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?
#
# "Puzzles from Wonderland." Lewis Carroll
#
# Nicola has solved this puzzle (and I am sure that you will do equally well).    To be prepared for more such puzzles, Nicola wants to invent a method to search for words inside poetry.    You can help him create a function to search for certain words.
#
# You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n).    Casing does not matter for your search, but whitespaces should be removed before your search.    You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines.    For this you need envision the rhyme as a matrix (2D array).    Find the coordinates of the word in the cut rhyme (without whitespaces).
#
# The result must be represented as a list --[row_start,column_start,row_end,column_end], where
#
# row_startis the line number for the first letter of the word.column_startis the column number for the first letter of the word.row_endis the line number for the last letter of the word.column_endis the column number for the last letter of the word.Counting of the rows and columns start from 1.
#
# Input:Two arguments. A rhyme as a string and a word as a string (lowercase).
#
# Output:The coordinates of the word.
#
# Precondition:The word is given in lowercase
# 0<|word|<10
# 0<|rhyme|<300
#
#
# END_DESC

import re
from itertools import zip_longest


def checkio(text, word):

    text, word = text.lower(), word.lower()

    rhyme = text.replace(" ", "").split("\n")

    print("h", rhyme)
    print("v", [''.join(x) for x in zip_longest(*rhyme, fillvalue='!')])

    for line in rhyme:
        if word in line:
            return [rhyme.index(line)+1, re.search(word, line).span()[0]+1, rhyme.index(line)+1, re.search(word, line).span()[1]]
    else:

        rhyme = [''.join(x) for x in zip_longest(*rhyme, fillvalue='!')]
        for line in rhyme:
            if word in line:
                return [re.search(word, line).span()[0]+1, rhyme.index(line)+1, re.search(word, line).span()[1], rhyme.index(line)+1]

    return None


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    assert checkio("xa\nxb\nx", "ab") == [1, 2, 2, 2]
