#!/usr/bin/env checkio --domain=py run box-probability

# https://py.checkio.org/mission/box-probability/

# To start the game they put several black and white pearls in one of the boxes.    Each robot hasNmoves, after which the initial set is being restored for the next game.    Each turn, the robot takes a pearl out of the box and puts one of the opposite color back.    The winner is the one who takes the white pearl on theNthmove.
#
# Our robots don't like uncertainty, that's why they want to know the probability of drawing a white pearl on the Nth move.    The probability is a value between 0 (0% chance or will not happen) and 1 (100% chance or will happen).    The result is a float from 0 to 1 with two decimal digits of precision (±0.01).
#
# You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the move    (N).    The order of the pearls does not matter.
#
#
#
# Input:The start sequence of the pearls as a string and the move number as an integer.
#
# Output:The probability for a white pearl as a float.
#
# Precondition:0<N ≤ 20
# 0<|pearls| ≤ 20
#
#
#
# END_DESC


def checkio(marbles, step):

    l = [[marbles, 1]]

    m = []

    c = len(marbles)

    prob = 0

    for s in range(0, step-1):

        for i in l:

            b_c = i[0].count('b')
            w_c = i[0].count('w')

            if 'b' in i[0]:
                b = i[0].replace('b', 'w', 1)
                m.append([b, b_c/c*i[1]])
            if 'w' in i[0]:
                w = i[0].replace('w', 'b', 1)
                m.append([w, w_c/c*i[1]])

        else:

            del l[:]
            l.extend(m)
            del m[:]

    else:

        for j in l:

            prob += j[1]*j[0].count('w')/c

    return round(prob, 2)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
