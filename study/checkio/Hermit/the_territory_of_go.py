#!/usr/bin/env checkio --domain=py run the-territory-of-go

# https://py.checkio.org/mission/the-territory-of-go/

# This is the second mission about theGo game. The first one is theEaten Go Stones.
# In this mission you will learn how to count territory in the Go. Pay attention that this mission is simplified compared to the real game rules (the tests are haven't cases where stones of one color is on the territory of the other player).
#
# So what is territory in the Go game? This is all unoccupied points which are surrounded by the complete and solid border of the stones of one color. It can be the form in the center of the board, which uses only own stones for bounds or it also can be form near the edge of the board and use this edge to complete the boundary. The complete and solid boundary is that one which consists of the stones connected to each other only vertically and horizontally. Also it should be 'closed'.
# Look at this picture that describes the input data and the 'territory' conception:
#
#
#
# Your task is to count the territory which belongs to the each player. For this example the answer is: {'B': 13, 'W': 12}.
#
# Input:Two-dimensional array (the list of the strings).
#
# Output:Dictionary with the amount of the territory of the each player.
#
# Precondition:
# Board - 9х9, 7x7, 5x5
#
#
# END_DESC


def territory(board):
    # replace this for solution
    return board


if __name__ == '__main__':
    print("Example:")
    print(territory(['++B++++++',
                     '+BB++++++',
                     'BB+++++++',
                     '+++++++++',
                     '+++++++++',
                     '++WWW++++',
                     '++W+W++++',
                     '++WWW++++',
                     '+++++++++']))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert territory(['++B++++++',
                      '+BB++++++',
                      'BB+++++++',
                      '+++++++++',
                      '+++++++++',
                      '++WWW++++',
                      '++W+W++++',
                      '++WWW++++',
                      '+++++++++']) == {'B': 3, 'W': 1}
    print("Coding complete? Click 'Check' to earn cool rewards!")
