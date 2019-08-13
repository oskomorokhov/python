#!/usr/bin/env checkio --domain=py run supply-stations

# https://py.checkio.org/mission/supply-stations/

# “Do not let your fire go out, spark by irreplaceable spark in the hopeless swamps of the not-quite, the not-yet,        and the not-at-all. Do not let the hero in your soul perish in lonely frustration for the life you deserved and        have never been able to reach. The world you desire can be won. It exists.. it is real.. it is possible.. it's        yours.”
# -- "Atlas Shrugged" by Ayn Rand
#
# We need to supply our new factory with four various resources from four different stations. For simplicity we will    name them 1st, 2nd, 3rd and 4th resources (we can leave the rest up to your imagination). For this we will need to    calculate four routes from the supply stations to the factory. Trucks will must deliver our supplies without    stopping and we can not build several layers roads. So the truck routes should not intersect.
#
# You are given a rectangular map divided by square cells.    The map is represented as a sequence of strings, where:
# - "." is a clear cell;
# - "X" is an obstacle (forest, lake, etc);
# - "1", "2", "3" or "4" are supply stations;
# - "F" is a factory.
#
# You are given a rectangular map divided by square cells. The map is represented as a sequence of strings, where:
# - "N" north (up);
# - "S" south (down);
# - "E" east (right);
# - "W" west (left);
# A route will be represented as a string with these letters.    The result should be as a sequence (list or tuple) of four routes from 1st to 4th.
#
#
#
# For the given example (image) the result will be described as:
# ["NEEEESSSWS",
#  "WSSSSSSSEEENNNNEN,
#  "NNNNEE",
#  "NNNNWWWW"]
#
#
# Input:The map as a tuple of strings.
#
# Output:The routes as a tuple/list of strings.
#
# Precondition:
# All test cases are solvable.
# 5 ≤ len(the_map) ≤ 10
# all(5 ≤ len(row) ≤ 10 for row in the_map)
#
#
#
# END_DESC


def supply_routes(the_map):
    return "", "", "", ""


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    DIRS = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }

    def checker(f, the_map):
        result = f(the_map)
        if (not isinstance(result, (tuple, list)) and len(the_map) != 4 and
                any(not isinstance(r, str) for r in the_map)):
            return False, "The result must be a list/tuple of four strings"
        stations = [None] * 4
        factory_supply = [0] * 4
        for i, row in enumerate(the_map):
            for j, ch in enumerate(row):
                if ch in "1234":
                    stations[int(ch) - 1] = (i, j)
        wmap = [list(row) for row in the_map]
        width = len(wmap[0])
        height = len(wmap)
        for numb, route in enumerate(result, 1):
            coor = stations[numb - 1]
            for i, ch in enumerate(route):
                if ch not in DIRS.keys():
                    return False, "Routes must contain only NSWE"
                row, col = coor[0] + DIRS[ch][0], coor[1] + DIRS[ch][1]
                if not (0 <= row < height and 0 <= col < width):
                    return False, "Ooops, we lost the route from station {}".format(numb)
                checked = wmap[row][col]
                if checked == "X":
                    return False, "The route {} was struck {} {}".format(numb, coor, (row, col))
                if checked == "F":
                    factory_supply[numb - 1] = 1
                    if i >= len(route):
                        return False, "A route should be ended in the factory"
                    break
                if checked != ".":
                    return False, "Don't intersect routes"
                wmap[row][col] = str(numb)
                coor = row, col
        if factory_supply != [1, 1, 1, 1]:
            return False, "You should deliver all four resources"
        return True, "Great!"

    test1 = checker(supply_routes, ("..........",
                                    ".1X.......",
                                    ".2X.X.....",
                                    ".XXX......",
                                    ".X..F.....",
                                    ".X........",
                                    ".X..X.....",
                                    ".X..X.....",
                                    "..3.X...4.",
                                    "....X....."))
    print(test1[1])
    assert test1[0], "First test"
    test2 = checker(supply_routes, ("1...2",
                                    ".....",
                                    "..F..",
                                    ".....",
                                    "3...4"))
    print(test2[1])
    assert test2[0], "Second test"
    test3 = checker(supply_routes, ("..2..",
                                    ".....",
                                    "1.F.3",
                                    ".....",
                                    "..4.."))
    print(test3[1])
    assert test3[0], "Third test"
