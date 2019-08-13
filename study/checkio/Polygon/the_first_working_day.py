#!/usr/bin/env checkio --domain=py run the-first-working-day

# https://py.checkio.org/mission/the-first-working-day/

# As the input you will get the date of the first day of the vacation in the format 'YYYY-MM-DD' and the number of days of the vacation. Your task is to find out which day will be the first working day after the vacation. If it will be Saturday or Sunday then it should be the next Monday.
# In this mission you should ignore the national holidays and consider only Saturdays and Sundays.
# Also don't forget about February 29th in the leap year and about the situation when the start of the vacation is at the end of the December of the one year and the end of it is at the beginning of the next year.
#
# Input:First day of the vacation and number of days of it.
#
# Output:Date of the first working day.
#
# Precondition:
# 1900<= year<= 2100
#
#
# END_DESC


def vacation(date, days):
    # replace this for solution
    return 0


if __name__ == '__main__':
    print("Example:")
    print(vacation('2018-07-01', 14))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert vacation('2018-07-01', 14) == '2018-07-16'
    assert vacation('2018-02-19', 10) == '2018-03-01'
    assert vacation('2000-02-28', 5) == '2000-03-06'
    assert vacation('1999-12-20', 14) == '2000-01-03'
    print("Coding complete? Click 'Check' to earn cool rewards!")
