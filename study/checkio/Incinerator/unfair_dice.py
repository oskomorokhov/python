#!/usr/bin/env checkio --domain=py run unfair-dice

# https://py.checkio.org/mission/unfair-dice/

# For this task, you'regoingto play a dice game, but first you must prepare for an overwhelming victory.    The game itself is very simple.    Both players roll a single die and whoever rolls highest scores a point.     (On a tie, both players must reroll until someone scores.)
#
# These aren't standard dice however.    Each player can put any positive number on any side of the die as long as the number of sides match    and the total of all the chosen numbers are the same.    For example, one player might use a six sided die with the numbers [3, 3, 3, 3, 6, 6]    while the other player uses a six sided die with the numbers [4, 4, 4, 4, 4, 4].    The interesting part of this game is that even with the same number of sides and the same total,    different dice have different chances of winning. Using the example die, the player with all 4's will win 2/3 of the time.
#
# To prepare for this game, you're investigating different ways of picking the numbers.    To do this, write a program that will take an opponent's die    and output some die which will win against it more than half the time.    If no die satisfies the task requirements, return an empty list.
#
# Input:An enemy's die as a sorted list of integers, one for each face of the opponent's die.
#
# Output:Your die as a list of integers, one for each face of your die or an empty list.
#
# Example:
#
#
# winning_die([3, 3, 3, 3, 6, 6]) == [4, 4, 4, 4, 4, 4] # Or [3, 3, 4, 4, 5, 5]
# winning_die([4, 4, 4, 4, 4, 4]) == [2, 2, 5, 5, 5, 5] # Or [5, 5, 2, 2, 5, 5]
# winning_die([2, 2, 5, 5, 5, 5]) == [3, 3, 3, 3, 6, 6]
# winning_die([1, 1, 3]) == [1, 2, 2]
# winning_die([1, 2, 3, 4, 5, 6]) == [] # Any 6-sided die totaling 21 has a 50/50 chance of winning against the standard die.
# winning_die([2, 3, 4, 5, 6, 7]) == [1, 1, 3, 7, 7, 8] # This can be beat though.
# winning_die([1, 2, 3, 4, 5, 6]) == []
# Preconditions:
# 3 ≤ len(die) ≤ 10
# sum(die) ≤ 100
# min(die) ≥ 1
# max(die) ≤ 18
#
#
# END_DESC


def winning_die(enemy_die):
    return []


if __name__ == '__main__':
    # These are only used for self-checking and not necessary for auto-testing
    def check_solution(func, enemy):
        player = func(enemy)
        total = 0
        for p in player:
            for e in enemy:
                if p > e:
                    total += 1
                elif p < e:
                    total -= 1
        return total > 0

    assert check_solution(winning_die, [3, 3, 3, 3, 6, 6]), "Threes and Sixes"
    assert check_solution(winning_die, [4, 4, 4, 4, 4, 4]), "All Fours"
    assert check_solution(winning_die, [1, 1, 1, 4]), "Unities and Four"
    assert winning_die([1, 2, 3, 4, 5, 6]) == [], "All in row -- No die"
