#!/usr/bin/env checkio --domain=py run oil-pie

# https://py.checkio.org/mission/oil-pie/

#
# END_DESC

from fractions import Fraction


def divide_pie(groups):

    drones = sum([abs(d) for d in groups])

    opie = cpie = Fraction(1/1)

    for d in groups:

        if d > 0:
            cpie = (cpie-(opie / drones * d))
        else:
            cpie = (cpie-(cpie / drones * abs(d)))

    return (0, 1) if str(cpie) == '0' else [int(x) for x in str(cpie).split('/')]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    assert tuple(divide_pie([15, 33, 37, 16, -1, 22, -73, 66, -59,
                             10, -39, 57])) == (2682139399739, 14362129722368)
