#!/usr/bin/env checkio --domain=py run unix-match

# https://py.checkio.org/mission/unix-match/

# Sometimes you find yourself in a situation where among a huge number of files on your computer or in a separate folder you need to find files of a certain type - for example, images with the extension '.jpg' or documents with the extension '.txt', or even files that have the word 'butterfly' in their name. Doing this manually can be time-consuming. 'Matching' or patterns for searching files by a specific mask are just what you need for these sort of challenges.
# This mission will help you understand how this works.
#
# You need to find out if the given unix pattern matches the given filename.
#
# Let me show you a couple of small examples of matching the filenames in the unix-shell. For example, * matches everything and *.txt matches all of the files that have txt extension. Here is a small table that shows symbols that can be used in patterns.
#
# *matches everything?matches any single character[seq]matches any character in seq[!seq]matches any character not in seqInput:Two arguments. Both are strings.
#
# Output:Bool.
#
#
# END_DESC


def unix_match(filename: str, pattern: str) -> bool:

    import re

    d = {'\.': '\.', '\*': '.*', '\?': '.',
         '\[\!([^]])': '[^\\1', '\[\!\]': '\[\!\]'}

    if pattern[0] == '[' and pattern[len(pattern)-1] == ']':

        pass

    else:

        for k, v in d.items():

            pattern = re.sub(k, v, pattern)
            print(pattern)

    print(pattern)

    try:

        return True if re.search('^'+pattern+'$', filename) else False

    except Exception as ex:

        return False


if __name__ == '__main__':
    print("Example:")
    # print(unix_match("[!]check.txt","[!]check.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing

    #assert unix_match("checkio","[c[]heckio") == True
    #assert unix_match("[!]check.txt","[!]check.txt") == True
    #assert unix_match("name.txt","name[]txt") == False
    #assert unix_match("[?*]","[[][?][*][]]") == True
    #assert unix_match("1name.txt","[!abc]name.txt") == True
    assert unix_match("1name.txt", "[!1234567890]*") == False
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
