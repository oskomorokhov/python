#!/usr/bin/env checkio --domain=py run time-converter-12h-to-24h

# https://py.checkio.org/mission/time-converter-12h-to-24h/

# You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places. Your task is to convert the time from the 12-h format into 24-h by following the next rules:
# - the output format should be 'hh:mm'
# - if the output hour is less than 10 - write '0' before it. For example: '09:05'
# Here you can find some useful information about the12-hour format.
#
#
#
# Input:Time in a 12-hour format (as a string).
#
# Output:Time in a 24-hour format (as a string).
#
# Precondition:
# '00:00'<= time<= '23:59'
#
#
# END_DESC


def time_converter(time):

    if 1 <= int(time[:time.index(':')]) < 12 and time[-1:-5:-1][::-1] == 'a.m.':
        time = '0'+time[0:time.index(' ')]
    elif int(time[:time.index(':')]) == 12 and time[-1:-5:-1][::-1] == 'a.m.':
        time = '00'+time[time.index(':'):time.index(' ')]
    elif 1 <= int(time[:time.index(':')]) < 12 and time[-1:-5:-1][::-1] == 'p.m.':
        time = str(int(time[:time.index(':')])+12) + \
            time[time.index(':'):time.index(' ')]
    elif int(time[:time.index(':')]) == 12 and time[-1:-5:-1][::-1] == 'p.m.':
        time = time[:time.index(' ')]
    return time


if __name__ == '__main__':
    print("Example:")
    #print(time_converter('12:30 a.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert time_converter('12:30 p.m.') == '12:30'
    #assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
