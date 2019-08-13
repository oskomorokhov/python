#!/usr/bin/env checkio --domain=py run unlucky-days

# https://py.checkio.org/mission/unlucky-days/

# Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.
#
# Find the number of Friday 13th in the given year.
#
# Input:Year as an integer.
#
# Output:Number of Black Fridays in the year as an integer.
#
# Precondition:1000<|year|<3000
#
#
# END_DESC

import datetime


def checkio(year):

    c = 0

    date = datetime.date(year, 1, 1)

    for d in range(0, 365):
        if (date+datetime.timedelta(days=d)).timetuple()[2] == 13 and (date+datetime.timedelta(days=d)).timetuple()[6] == 4:
            c += 1

    return c


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
