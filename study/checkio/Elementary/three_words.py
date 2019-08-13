#!/usr/bin/env checkio --domain=py run three-words

# https://py.checkio.org/mission/three-words/

# Let's teach the Robots to distinguish words and numbers.
#
# You are given a string with words and numbers separated by whitespaces (one space).    The words contains only letters.    You should check if the string contains three words insuccession.    For example, the string "start 5one two three7 end" contains three words in succession.
#
# Input:A string with words.
#
# Output:The answer as a boolean.
#
# Precondition:The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100
#
#
# END_DESC


def checkio(words):

    words = words.split()
    succession = []
    for index, word in enumerate(words):
        if not word.isdigit():
            succession.append(index)
    if succession == [] or len(succession) < 3:
        return False
    for item in succession:
        if item == succession[succession.index(item)+2]-2:
            return True
        if len(succession)-(succession.index(item)+1) < 3:
            return False
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("He is 123 man") == False
    assert checkio(
        "one two 3 four five 6 seven eight 9 ten eleven 12") == False
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
