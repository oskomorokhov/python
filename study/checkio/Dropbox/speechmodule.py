#!/usr/bin/env checkio --domain=py run speechmodule

# https://py.checkio.org/mission/speechmodule/

# Stephen's speech module is broken.    This module is responsible for his number pronunciation.    He has to click to input all of the numerical digits in a figure,    so when there are big numbers it can take him a long time.    Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.    All the words in the string must be separated by exactly one space character.    Be careful with spaces -- it's hard to see if you place two spaces instead one.
#
# Input:A number as an integer.
#
# Output:The string representation of the number as a string.
#
# How it is used:This concept may be useful for the speech synthesis software or automatic reports systems.    This system can also be used when writing a chatbot by assigning words or phrases numerical    values and having a system retrieve responses based on those values.
#
# Precondition:0 < number < 1000
#
#
# END_DESC

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    if number < 10:
        return FIRST_TEN[number-1]
    elif number < 20:
        return SECOND_TEN[number-10]
    elif number % 10 == 0 and number < 100:
        return OTHER_TENS[number//10-2]
    elif number % 100 == 0:
        return FIRST_TEN[(number//100)-1]+' '+HUNDRED
    elif 20 < number < 100:
        return OTHER_TENS[number//10-2]+' '+FIRST_TEN[number % 10-1]
    else:
        return FIRST_TEN[(number//100)-1]+' '+HUNDRED+' '+checkio(number % 100)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(39) == 'thirty nine', "7th example"
    assert checkio(100) == 'one hundred', "8th example"
    assert not checkio(212).endswith(
        ' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
