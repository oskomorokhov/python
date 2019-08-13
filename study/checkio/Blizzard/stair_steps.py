#!/usr/bin/env checkio --domain=py run stair-steps

# https://py.checkio.org/mission/stair-steps/

# There is a staircase with N steps and two platforms; one at the beginning, the other at the end of the stairs.     On each step a number is written (ranging from -100 to 100 with the exception of 0.)    Zeros are written on both platforms.    You start going up the stairs from the first platform, to reach the top on the second one.    You can move either to the next step or to the next step plus one.    You must find the best path to maximize the sum of numbers on the stairs on your way up and return the final sum.
#
#
#
# Input:Numbers on each stair as a list of integers.
#
# Output:The final sum for the best way as an integer.
#
# Precondition:
# 0 < len(steps) ≤ 10
# all(-100 < x < 100 and x for x in steps)
#
#
# END_DESC


def checkio(numbers):

    numbers = [0]+numbers+[0]

    for n in range(2, len(numbers)):
        numbers[n] += max(numbers[n-1], numbers[n-2])

    return numbers[-1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35,
                    27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    print('All ok')
