#!/usr/bin/env checkio --domain=py run zigzag-array

# https://py.checkio.org/mission/zigzag-array/

# This function creates a List of lists. that represents a two-dimensional grid with the given number of rows and  cols . This grid should contain the integers fromstarttostart + rows * cols - 1in ascending order, but so that the elements of every odd-numbered row are listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
#
# Input:Two ints rows and cols. And one optional argument start.
#
# Output:List of lists.
#
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
#
#
# END_DESC

from typing import List


def create_zigzag(rows: int, cols: int, start: int = 0) -> List[List[int]]:
    # your code here
    return []


if __name__ == '__main__':
    print("Example:")
    print(create_zigzag(2, 3, 5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert create_zigzag(3, 5) == [
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7, 6],
        [11, 12, 13, 14, 15]
    ]
    assert create_zigzag(5, 1) == [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
    assert create_zigzag(2, 3, 5) == [
        [5, 6, 7],
        [10, 9, 8],
        [11, 12, 13]
    ]

    # Edge cases
    assert create_zigzag(0, 3) == []
    assert create_zigzag(3, 0) == []
    assert create_zigzag(0, 0) == []

    print("Coding complete? Click 'Check' to earn cool rewards!")
