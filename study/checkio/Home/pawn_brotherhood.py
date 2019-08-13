#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# https://py.checkio.org/mission/pawn-brotherhood/

#
# END_DESC

import string


def safe_pawns(pawns):

    a = string.ascii_lowercase
    counter = 0
    for pawn in pawns:
        sw = a[a.index(pawn[0])-1]+str(int(pawn[1])-1)
        se = a[a.index(pawn[0])+1]+str(int(pawn[1])-1)
        if sw in pawns or se in pawns:
            counter += 1
    return counter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
