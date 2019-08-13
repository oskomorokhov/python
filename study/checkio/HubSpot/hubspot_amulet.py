#!/usr/bin/env checkio --domain=py run hubspot-amulet

# https://py.checkio.org/mission/hubspot-amulet/

# table.matrix {    border-left: solid; border-right: solid; font-weight: bold;    margin: 10px    }    table.matrix td{    padding: 2px;        text-align: center;    }While exploring the island, Sofia found an interesting Amulet.    Along the perimeter of the amulet small points are marked on each degree (for a total 360 degrees.)    Three levers extrude from the amulet with varying lengths.     The first lever is the shortest, the second lever is in the middle of the three and the last is the longest.    These levers can be rotated, but if you rotate one lever the others rotate as well.    The levers rotate discretely by degrees, rotating them clockwise gives you a positive angle while counterclockwise is negative.
#
# After some experiments Sophie discovers the levers correlation. If you rotate a lever, the other rotates in the same direction but with different speed.
# If you rotate the first, then the second is rotatedf2times faster, the third -- at thef3time faster.
# If you rotate the second, then the third is rotateds3times faster, the first -- at thes1time faster.
# If you rotate the third, then the first is rotatedt1times faster, the second -- at thet2time faster.
# This correlation can be represented as a matrix 3x3 with1in the main diagonal.
# 1f2f3s11s3t1t21For example, the rotating correlation is given as the matrix:123312231This means that:
# If you rotate the first, the second is rotated at double the angle while the third rotates at triple.
# If you rotate the second, the third is rotated at double the angle, and the first rotates at triple.
# If you rotate the third, the first is rotated at double the angle, and the second rotates at triple.
# For example: You rotate the first lever at +10 degrees.    As a result, the second is rotated at +20 degrees and the third at +30 degrees.You can rotate the levers from -180 to +180 degrees only (but in interrelated mode it can be rotated more than 360 degrees).    You can rotate each lever once in the following order: the first, the second, the third.    Sophie used her X-ray vision and found out what position each lever should be in.     After completing these rotations, the levers must be at0, 225, 315.
#
# You are given a rotation matrix as a list of lists with positive integers and the unitary main diagonal.    You should return a list of three integers -- the angles for each lever.    The start position of the levers is [0, 0, 0].
#
#
#
# Input:A rotation matrix as a list of lists.
#
# Output:The angles as a list of integers.
#
# Precondition:∀ x ∈ matrix : 0<x<10
# |matrix| = 3x3
#
#
# END_DESC


def checkio(matrix):

    for f in range(-180, 180+1):
        for s in range(-180, 180+1):
            for t in range(-180, 180+1):

                temp = [0, 0, 0]
                temp[0] += f
                temp[1] += matrix[0][1] * f
                temp[2] += matrix[0][2] * f

                temp[0] += matrix[1][0] * s
                temp[1] += s
                temp[2] += matrix[1][2] * s

                temp[0] += matrix[2][0] * t
                temp[1] += matrix[2][1] * t
                temp[2] += t
                temp = [n % 360 for n in temp]
                # print([f,s,t])
                if temp == [0, 225, 315]:
                    return [f, s, t]

    return [0, 0, 0]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False

    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"
