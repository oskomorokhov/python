#!/usr/bin/env checkio --domain=py run place-queens

# https://py.checkio.org/mission/place-queens/

# Almost everyone in the world knows about the ancient gameChessand has at least a basic understanding of its rules.    Ancient humans loved this game of skill and strategy and    our Robots are attempting to examine all tricks to becoming Chess Grandmasters.    Today they are trying to solve the 8-Queen problem as written in an old chess-manuscript.
#
# Chess is a two-player strategy game played on a checkered game board laid out in eight rows    (called ranks and denoted with numbers 1 to 8) and    eight columns (called files and denoted with letters a to h) of squares.    Each square of the chessboard is identified by a unique coordinate pair    — a letter and a number (ex, "a1", "h8", "d6").    For this mission we only need to concern ourselves with Queens.    The Queen can move any number of squares along the rank, file, or diagonal axis.
#
# You should place eight chess Queens on an 8×8 chessboard so that no two Queens threaten each other.    For this challenge, we have already placed one or more Queens on the board,    so you will need to finish the placement.    In addition, each Queen may be considered as part of it’s army,    meaning every Queen could possible be a threat to every other Queen on the board.
#
# You are given a set of square coordinates where we have placed Queens already.    You should finish this set and return the full set of the coordinates for all eight Queens.    If it's not possible -- return an empty set.
# Be careful - an initial position could possibly threaten another Queen right off the bat.
#
#
#
# Input:Placed Queens coordinates as a set of strings.
#
# Output:Eight Queens coordinates as a set of strings or an empty set.
#
# Precondition:
# 0 < placed < 8
#
#
#
# END_DESC


def place_queens(placed):
    return set()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations
    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
        for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    assert checker(place_queens, {"b2", "c4", "d6",
                                  "e8", "a7", "g5"}, False), "2nd Example"
