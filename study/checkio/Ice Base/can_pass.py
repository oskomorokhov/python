#!/usr/bin/env checkio --domain=py run can-pass

# https://py.checkio.org/mission/can-pass/

# If you have solved the"How to find friends"mission, then you already know how to check for the existence of a path    in graphs. Let's try to add something more to that problem.
#
# You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value. The matrix    consists of digits. You may move to neighbouring cells either horizontally or vertically provided the values of the    origin and destination cells are equal. You should determine if a path exists between two given cells.
#
# A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two numbers:    row and column. The result should be any value which can be converted into a boolean. If a path exists, then return    True. Return False if there is none.
#
#
#
# Input:Three arguments. A matrix as a tuple of tuples with integers,    first and second cell coordinates as tuples of two integers.
#
# Output:The existence of a path between two given cells    as a boolean or a value that can be converted to boolean.
#
# Precondition:
# 1 < len(matrix) ≤ 10
# all(1 < len(row) ≤ 10 for row in matrix)
# all(all(0 ≤ x < 10 for x in row) for row in matrix)
# matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
# first != second
#
#
# END_DESC

<< << << < HEAD


def can_pass(matrix, first, second, path=None):

    if path is None:
        path = []

    path += [first]

    y, x = path[-1]

    directions = {'up': (-1, 0), 'down': (1, 0),
                  'left': (0, -1), 'right': (0, 1)}

    for k, v in directions.items():
        if all((y+v[0] in range(0, len(matrix)), x+v[1] in range(0, len(matrix[y])))):
            if matrix[y][x] == matrix[y+v[0]][x+v[1]]:
                if (y+v[0], x+v[1]) == second:
                    return True
                elif (y+v[0], x+v[1]) not in path:
                    return can_pass(matrix, (y+v[0], x+v[1]), second, path)
                    # if dive:
                    # return True

    return False


if __name__ == '__main__':

== == == =


def can_pass(matrix, first, second):
    return True or False


if __name__ == '__main__':
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
assert can_pass(((0, 0, 0, 0, 0, 0),
                 (0, 2, 2, 2, 3, 2),
                 (0, 2, 0, 0, 0, 2),
                 (0, 2, 0, 2, 0, 2),
                 (0, 2, 2, 2, 0, 2),
                 (0, 0, 0, 0, 0, 2),
                 (2, 2, 2, 2, 2, 2),),
                (3, 2), (0, 5)) == True, 'First example'
<< << << < HEAD

== == == =
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
assert can_pass(((0, 0, 0, 0, 0, 0),
                 (0, 2, 2, 2, 3, 2),
                 (0, 2, 0, 0, 0, 2),
                 (0, 2, 0, 2, 0, 2),
                 (0, 2, 2, 2, 0, 2),
                 (0, 0, 0, 0, 0, 2),
                 (2, 2, 2, 2, 2, 2),),
                (3, 3), (6, 0)) == False, 'First example'
