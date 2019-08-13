#!/usr/bin/env checkio --domain=py run super-root

# https://py.checkio.org/mission/super-root/

# Square roots, cube roots, 4th roots... each are too boring for Nicola.    He needs to find the super root! With your help he will almost certainly find it.
#
# The super root of a numberNis the numberx,    such thatxx=N.
#
# The result should be accurate so thatxx≈ N±0.001.    OrN - 0.001 < xx< N + 0.001.
#
# Input:A number (N) as an integer.
#
# Output:The super root (x) as a float or an integer.
#
# Precondition:
# 1 ≤ number ≤ 10 ** 10
#
#
# END_DESC

import math


def super_root(number):
    '''
    Loop through x**x generator, immediately return the result if there is a perfect match
    If we've gone too far, start Newton-Raphson subroutine with previous value of x and return its result
    '''
    for x in i_2_power_i(number):
        if x[1] == number:
            return x[0]
        elif x[1] > number:
            z = x[0]-1
            break
    return newton_raphson(z, number)


def i_2_power_i(number):
    '''
    This subroutine (generator) is required to get initial estimate of x**x
    sqrt(number)+2 was picked as an arbitary upper boundary for the generator
    '''
    c = 0
    for x in range(1, int(math.sqrt(number))+2):
        c += 1
        yield c, x**x


def newton_raphson(x, number):
    '''
    https://en.wikipedia.org/wiki/Newton%27s_method
    '''
    while not (number-0.001 < x**x < number+0.001):
        foo = x**x-number
        dfoo = x**x*(math.log(x)+1)
        x = x-(foo/dfoo)
    return x


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
