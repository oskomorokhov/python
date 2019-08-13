#!/usr/bin/env checkio --domain=py run triangle-angles

# https://py.checkio.org/mission/triangle-angles/

# You are given the lengths for each side on a triangle.    You need to find all three angles for this triangle.    If the given side lengths cannot form a triangle (or form a degenerated triangle),    then you must return all angles as 0 (zero).    The angles should be represented as a list of integers inascending order.    Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).
#
#
#
# Input:The lengths of the sides of a triangle as integers.
#
# Output:Angles of a triangle in degrees as sorted list of integers.
#
# Precondition:
# 0 < a,b,c ≤ 1000
#
#
# END_DESC

import math


def checkio(a=None, b=None, c=None):

    l = []

    if not (a and b and c):
        return [0, 0, 0]

    if a == b == c:
        return [60, 60, 60]

    def isosceles(s1, s3):
        try:
            l.append(round(2*(math.degrees(math.asin(s3/2/s1)))))
        except:
            return [0, 0, 0]
        l.append(round((180-l[:].pop())/2))
        l.append(l[:].pop())
        return l

    if a == b:
        l = isosceles(b, c)
    elif b == c:
        l = isosceles(c, a)
    elif a == c:
        l = isosceles(c, b)
    else:
        l = sorted((a, b, c), reverse=True)
        try:
            l.append(
                round(math.degrees(math.acos((l[1]**2+l[2]**2-l[0]**2)/(2*l[1]*l[2])))))
            l.append(
                round(math.degrees(math.acos((l[0]**2+l[2]**2-l[1]**2)/(2*l[0]*l[2])))))
            l.append(
                round(math.degrees(math.acos((l[0]**2+l[1]**2-l[2]**2)/(2*l[0]*l[1])))))
        except:
            return [0, 0, 0]
        l = l[3:]

    if sum(l) > 180 or 0 in l:
        return [0, 0, 0]
    else:
        return sorted(l)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    #assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    #assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    #assert checkio(80,80,60) == [44,68,68]
    #assert checkio(395,295,295) == [48,48,84]
    print("all done, time to check!")
