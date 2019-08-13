#!/usr/bin/env checkio --domain=py run find-sequence

# https://py.checkio.org/mission/find-sequence/

# “There’s nothing here...” sighed Nikola.
#
# “You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” SaidSofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.
#
# “Where did you get-”
#
# “Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.
#
# CLUNK
#
# “Hey we hit something.” Stephen exclaimed in surprise.
#
# “It’s the treasure!” Sofia was jumping up and down in excitement.
#
# The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing        the lid but it was locked. Nikola studied the locking mechanism.
#
# “I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4        or more matching numbers and output a bool.”
#
# “Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.
#
# You are given a matrix of NxN (4≤N≤10).    You should check if there is a sequence of 4 or more matching digits.    The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
#
# Input:A matrix as a list of lists with integers.
#
# Output:Whether or not a sequence exists as a boolean.
#
# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)
#
#
# END_DESC


def checkio(matrix):

    def check_matrix(matrix):

        for l in matrix:
            c = 1
            for j, i in enumerate(l[:-1]):
                if i == l[j+1]:
                    c += 1
                if c >= 4:
                    return True
                if i != l[j+1] and c != 0:
                    c = 1
        return False

    diag = []
    offset = 0

    while offset <= len(matrix[0])-4:
        diag.append([row[i+offset]
                     for i, row in enumerate(matrix) if 0 <= i+offset < len(row)])
        diag.append([row[i-offset]
                     for i, row in enumerate(matrix) if 0 <= i-offset < len(row)])
        diag.append([row[-i-1+offset]
                     for i, row in enumerate(matrix) if 0 <= i-offset < len(row)])
        diag.append([row[-i-1-offset]
                     for i, row in enumerate(matrix) if 0 <= i+offset < len(row)])
        offset += 1

    return True if (check_matrix(matrix) or check_matrix(zip(*matrix)) or check_matrix(diag)) else False


if __name__ == '__main__':

    assert checkio([[1, 9, 7, 8, 9, 3, 6, 5, 6, 2], [4, 9, 4, 8, 3, 4, 8, 8, 5, 9], [2, 8, 5, 5, 7, 8, 6, 1, 3, 6], [6, 4, 7, 6, 9, 1, 4, 5, 7, 8], [4, 7, 7, 9, 8, 8, 8, 8, 4, 4], [
                   3, 7, 3, 2, 1, 9, 1, 8, 9, 1], [4, 7, 2, 4, 8, 1, 2, 3, 6, 2], [4, 4, 1, 3, 3, 3, 9, 2, 6, 7], [8, 6, 1, 9, 3, 5, 8, 1, 7, 5], [7, 3, 6, 5, 3, 6, 6, 4, 8, 2]]) == True

    print("All done, press check!")
