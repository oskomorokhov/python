#!/usr/bin/env checkio --domain=py run house-password

# https://py.checkio.org/mission/house-password/

#
# END_DESC

import string
import re


def checkio(data):

    flags = [False]*4
    if len(data) >= 10:
        flags.remove(False)
        flags.append(True)
    if re.search('\d', data):
        flags.remove(False)
        flags.append(True)
    if re.search('[A-Z]', data):
        flags.remove(False)
        flags.append(True)
    if re.search('[a-z]', data):
        flags.remove(False)
        flags.append(True)
    return (True if flags.count(True) == 4 else False)

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
