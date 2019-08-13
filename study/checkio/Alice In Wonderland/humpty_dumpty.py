#!/usr/bin/env checkio --domain=py run humpty-dumpty

# https://py.checkio.org/mission/humpty-dumpty/

# .story.shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;    }
# END_DESC

import math


def checkio(height, width):

    a = width/2
    c = height/2

    if c < a:

        e = math.sqrt(1-c**2/a**2)
        S = 2*math.pi*(a**2)*(1+(1-e**2)*math.atanh(e)/e)

    elif c > a:

        e = math.sqrt(1-a**2/c**2)
        S = 2*math.pi*a**2*(1+(c*math.asin(e)/(a*e)))

    else:

        S = 4*math.pi*c**2

    V = ((4*math.pi)/3)*a**2*c

    return [round(V, 2), round(S, 2)]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
