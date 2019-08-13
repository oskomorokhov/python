#!/usr/bin/env checkio --domain=py run the-most-frequent-weekdays

# https://py.checkio.org/mission/the-most-frequent-weekdays/

# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
#
# You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year.    The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.
#
# Input:Year as anint.
#
# Output:The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
#
# Preconditions:Year is between 1 and 9999. Week starts with Monday.
#
#
# END_DESC

import datetime
import calendar


def most_frequent_days(year):

    week_days = list(calendar.day_name)
    week_days_count = [0 for x in range(0, 7)]

    date = datetime.date(year, 1, 1)
    week_days_count[date.timetuple()[6]] += 1

    while date < datetime.date(year, 12, 31):
        date += datetime.timedelta(days=1)
        week_days_count[date.timetuple()[6]] += 1

    return [x for i, x in enumerate(week_days) if week_days_count[i] == max(week_days_count)]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
