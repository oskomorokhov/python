#!/usr/bin/env checkio --domain=py run count-neighbours

# https://py.checkio.org/mission/count-neighbours/

# "Animals and plants can reproduce themselves,        but it was only recently shown that machines can be made which also        reproduce themselves... Other kinds of self-reproducing machines        will be described, and one simple mechanical        model, with no electrical or magnetic complications,        will be there in working order for the audience to inspect and operate."
#
# -- Edward Forrest Moore
#
# In cellular automata,the    Moore neighborhoodcomprises    the eight cells surrounding a central cell on a two-dimensional square lattice.    The neighborhood is named after Edward F. Moore, a pioneer of cellular automata theory.    Many board games are played with a rectangular grid with squares as cells.    For some games, it is important to know about the conditions of neighbouring cells for chip    (figure, draught etc) placement and strategy.
#
# You are given a state for a rectangular board game grid with chips in a binary matrix, where 1    is a cell with a chip and 0 is an empty cell. You are also given the coordinates for a cell in    the form of row and column numbers (starting from 0). You should determine how many chips are    close to this cell. Every cell interacts with its eight neighbours; those cells that are    horizontally, vertically, or diagonally adjacent.
#
#
#
# For the given examples (see the schema) there is the same grid:
#
#
# ((1, 0, 0, 1, 0),
#  (0, 1, 0, 0, 0),
#  (0, 0, 1, 0, 1),
#  (1, 0, 0, 0, 0),
#  (0, 0, 1, 0, 0),)
#
# For the first example coordinates of the cell is (1, 2) and    as we can see from the schema this    cell has 3 neighbour chips.    For the second example coordinates is (0, 0) and this cell contains    a chip, but we count only neighbours and the answer is 1.
#
# Input:Three arguments. A grid as a tuple of tuples with integers (1/0),    a row number and column number for a cell as integers.
#
# Output:How many neighbouring cells have chips as an integer.
#
#
# Precondition:
# 3 ≤ len(grid) ≤ 10
# all(len(grid[0]) == len(row) for row in grid)
#
#
# END_DESC


def count_neighbours(grid, row, col):

    neighbors = {'nw': [-1, -1], 'n': [-1, 0], 'ne': [-1, 1],
                 'e': [0, 1], 'se': [1, 1], 's': [1, 0], 'sw': [1, -1], 'w': [0, -1]}

    cells = 0

    for n in neighbors:

        if not any((len(grid) <= row+neighbors[n][0], row+neighbors[n][0] < 0, len(grid[row]) <= col+neighbors[n][1], col+neighbors[n][1] < 0)):
            cells += grid[row+neighbors[n][0]][col+neighbors[n][1]]

    return cells


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
