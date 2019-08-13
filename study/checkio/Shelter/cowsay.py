#!/usr/bin/env checkio --domain=py run cowsay

# https://py.checkio.org/mission/cowsay/

# ul.rules li {        margin-left: 20px;    }Lets cow say!
#
#
# Our cow is young and can only say some of the words we teach it.    Not only does it talk, but this cow can turn into the famous Tux    (wiki/Cowsay) if we ask it nicely.
#
# You are given some text and your function should format it in the "cows" speech.    Let's examine the rules for this problem:The cow is always the same, only quote changes.Multiple spaces in a row are replaced by one space.The top border consists of underscore characters. It starts from a single space and ends before the border column.Each line of the quote consists of these parts: quote border(1), space(1), line(1-39), space(1), quote border(1).If line is less than 40 characters, it will fit into one string. The string is quoted in<>.If the line is greater than or equal to 40 characters, it should be split by these rules:Max line size is 39 chars. If any spaces are in the line,                    split it by the rightmost space (this space is removed from text) otherwise take the first 39 characters.After the split align all lines to same length by adding spaces at the end of each line.First line borders:/\Middle line borders:||Last line borders:\/The bottom border consists of the minus sign. Has same length as top.cowsay console program has strange behavior in certain cases, this cases will not be tested here.
#      _________________________________
#     / Dog goes woof                   \
#     | Cat goes meow                   |
#     | Bird goes tweet                 |
#     | And mouse goes squeek           |
#     | Cow goes moo                    |
#     | Duck goes quack                 |
#     \ And the solution will go to you /
#      ---------------------------------
#             \   ^__^
#              \  (oo)\_______
#                 (__)\       )\/\
#                     ||----w |
#                     ||     ||
#     What does the cow say?
# Input:Text as a string.
#
# Output:The result for the console as a string.
#
# Hint:Read python docs (2.7,3.3)    about formatting styles (str.format and %).    Notice forrbefore the string. It is a raw string and they use different rules for interpreting backslash    escape sequences.
#
# Precondition:0 < len(text) < 858;
# textcan't consist of spaces only;
# textcontains only ASCII letters, digits and punctuation.
#
#
# END_DESC

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    return 'Cow say "%s"' % text


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                               'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
