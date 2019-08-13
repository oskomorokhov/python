#!/usr/bin/env checkio --domain=py run when-is-friday

# https://py.checkio.org/mission/when-is-friday/

# Friday is an awesome day. It's the end of the week after which you can just relax and attend to all of the things you've been pushing away. It's really good to know how many days you still have to wait, isn't it?
#
# Your task is to write a function that will count how many days are left from a certain date to Friday. The argument will be a particular date in a string format looking like this: 'dd.mm.yyyy', where 'dd' - day, 'mm' - month, and 'yyyy' - year.
# For example, if that given day is Thursday, then the answer will be 1. If that day is Monday, the result is 4. And if that day is Friday, the function should return 0.
#
#
#
# Input:Date as a string.
#
# Output:The amount of days left until Friday.
#
# Precondition:
# 1<= year<= 3000
#
#
# END_DESC

from datetime import datetime


def friday(day):

    wd = datetime.strptime(day, "%d.%m.%Y").weekday()

    return 0 if wd == 4 else (4-wd if 0 <= wd < 4 else 7-wd+4)


if __name__ == '__main__':
    # print("Example:")
    # print(friday('23.04.2018'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
