#!/usr/bin/env checkio --domain=py run supply-line

# https://py.checkio.org/mission/supply-line/

# Many war games have rules concerning the supply lines.Units that can’t contact the supply source face a lot of  troubles.
#
# You should find the shortest supply line with Python.
#
# The map used in this mission is a hex grid with a maximum size of 12x9 where each hex is numbered from A1 to L9.(A - L indicate a column, and 1 - 9 indicate a row.)
#
#
#
# You are given three arguments: the first is the position of your uint (a string), the second is the supply depots (the set of strings), and the third is the enemy units (the set of strings).You should return the minimum number of steps from your unit to the supply depot.If you can’t set a supply line at all, return None.
#
# The effect of the enemy hex and its adjacent hexes:
#
# You can’t lay the supply lines on these hexes.If your unit is adjacent to the enemy’s, there is no problem with the supply line.The supply depot on these hexes can’t be used .
#
# Input:Three arguments. The first one is the position of your unit as a string, the second one is the supply depots as the set of strings, the third one is the enemy units as the set of strings.
#
# Output:The minimum number of steps from your unit to the supply depot as an integer (or None).
#
# How it is used:
# In war games. Searching for a path is important for movement and getting supplies.And the idea of the adjacent hex cells is often seen as aZone of control(ZOC).
#
# Precondition:
# all(map(lambda x: re.match('[A-L][1-9]$', x), {you} | depots | enemies))you not in depots | enemieslen(depots) > 0len(enemies) ≥ 0
#
#
# END_DESC


def supply_line(you, depots, enemies):

    # replace this for solution
    return 0


if __name__ == '__main__':
    assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
    assert supply_line("A3", {"A9", "F5", "G8"}, {
                       "B3", "G6"}) == 11, 'multiple'
    assert supply_line("C2", {"B9", "F6"}, {
                       "B7", "E8", "E5", "H6"}) is None, 'None'
    assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
    assert supply_line("A5", {"A2", "B9"}, {
                       "B3", "B7", "E3", "E7"}) == 13, '2 depots'
    print('"Run" is good. How is "Check"?')
