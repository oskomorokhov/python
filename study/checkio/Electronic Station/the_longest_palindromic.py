#!/usr/bin/env checkio --domain=py run the-longest-palindromic

# https://py.checkio.org/mission/the-longest-palindromic/

# Write a function that finds the longestpalindromicsubstring of a given string. Try to be as efficient as possible!
#
# If you find more than one substring you should return the one which is closer to the beginning.
#
# Input:A text as a string.
#
# Output:The longest palindromic substring.
#
# Precondition:1<|text| ≤ 20
# The text contains only ASCII characters.
#
#
# END_DESC


def longest_palindromic(text):

    if len(set(text)) == 1:
        #print("All the same")
        return text

    l = []

    def rec_text(text):

        if len(text) <= 2:
            #print("text len <=2, end")
            return False

        for i in range(2, len(text)):

            print("pieces:", text[:i], text[i-1::-1])
            if text[:i] == text[i-1::-1]:
                print("found polindrom", text[:i])
                l.append(text[:i])
        else:
            #print("loop end, cut & recur")
            text = text[1:]
            rec_text(text)

    rec_text(text)

    print(l)
    return sorted(l, key=len, reverse=True)[0] if l else text[0]


if __name__ == '__main__':
    #assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    #assert longest_palindromic("abacada") == "aba", "The First"
    #assert longest_palindromic("aaaa") == "aaaa", "The A"
    #assert longest_palindromic("abc") == "a"
    assert longest_palindromic("aba") == "aba"

    print("all done, time to check!")
