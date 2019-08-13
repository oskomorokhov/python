#!/usr/bin/env checkio --domain=py run nonogram-row

# https://py.checkio.org/mission/nonogram-row/

# The 'nonogaram' an exceptional mind-sharpening grid puzzle which requires for you to  identify all cells in the grid as 'filled' or 'empty'.
#
# For this mission you are given a row (String) and the number clues (list of Integers), so you will have to work with just one line.Each number clue represents the length of filled cells which will appear in that exact order.
# If you'll manage to identify more filled or empty cells, reflect them in the input string and return it. If the row and number clues don't match, return None.
#
# Symbol details:'?' : unknown cell.'O' : filled cell.'X' : empty cell.Input:two arguments, an input row (String), and the number clues (list of Integers)
#
# Output:the result row (String) or None
#
# How it is used:
# The actual nonogaram puzzle consists of multiple rows and also have number clues for the columns. All nonogram puzzles are designed in a way that all of the cells are identified as 'filled' or 'empty' with the help of the given number clues.
#
#
#
# Precondition:
# all(r in ('?', 'O', 'X') for r in row_string)all(0 ≤ cn ≤ len(row_string) for cn in clue_numbers)sum(clue_numbers) + len(clue_numbers) - 1 ≤ len(row_string)
#
#
# END_DESC


def nonogram_row(row_string, clue_numbers):
    return ''


if __name__ == '__main__':
    assert nonogram_row('??????????', [8]) == '??OOOOOO??', 'Simple boxes_1'
    assert nonogram_row('??????????', [4, 3]) == '??OO???O??', 'Simple boxes_2'
    assert nonogram_row('???O????O?', [3, 1]) == 'X??O??XXOX', 'Simple spaces'
    assert nonogram_row('????X?X???', [3, 2]) == '?OO?XXX?O?', 'Forcing'
    assert nonogram_row('O?X?O?????', [1, 3]) == 'OXX?OO?XXX', 'Glue'
    assert nonogram_row('??OO?OO???O?O??', [
                        5, 2, 2]) == 'XXOOOOOXXOOXOOX', 'Joining and splitting'
    assert nonogram_row('????OO????', [4]) == 'XX??OO??XX', 'Mercury'
    assert nonogram_row('???X?', [0]) == 'XXXXX', 'Empty_1'
    assert nonogram_row('?????', []) == 'XXXXX', 'Empty_2'
    assert nonogram_row('??X??', [3]) is None, 'Wrong string'
    print("Check done.")
