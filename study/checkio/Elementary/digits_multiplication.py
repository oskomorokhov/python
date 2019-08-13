#!/usr/bin/env checkio --domain=py run digits-multiplication

# https://py.checkio.org/mission/digits-multiplication/

# You are given a positive integer.    Your function should calculate the product of the digits excluding any zeroes.
#
# For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
#
# Input:A positive integer.
#
# Output:The product of the digits as an integer.
#
# Precondition:0 < number < 106
#
#
# END_DESC


def checkio(number):
    number = str(number).replace("0", "1")
    number = [i for i in number]
    c = 1
    for i in number:
        c = c*int(i)
    return c


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
