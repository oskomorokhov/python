#!/usr/bin/env checkio --domain=py run the-nearest-square-number

# https://py.checkio.org/mission/the-nearest-square-number/

# You have some number and you are trying to find the nearest square number (a perfect square). Square number is the number the square root of which is an integer. For example, if we start with the number 8, then the two nearby square numbers are 4 (sqrt(4) == 2) and 9 (sqrt(9) == 3). So the answer is 9, because 9 is the nearest.
#
#
#
#
#
# Input:A number.
#
# Output:The nearest square number.
#
# Precondition:
# 0<number<= 1000000
#
#
#
# END_DESC


def nearest_square(number):
    # replace this for solution
    return 0


if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")
