#!/usr/bin/env checkio --domain=py run friendly-number

# https://py.checkio.org/mission/friendly-number/

#
# END_DESC


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):

    import math

    c = 0

    while abs(number) >= base and c < len(powers)-1:
        number = float(number)/base
        c += 1
        print(c, number)

    if decimals == 0:
        number = math.floor(number) if number > 0 else math.ceil(number)

    else:
        number = float(number)
        number = round(number, decimals) if len(str(number)[str(number).index('.')+1:]) > decimals else str(
            round(number, decimals))+'0'*(decimals-len(str(number)[str(number).index('.')+1:]))

    return str(number)+powers[c]+suffix if number != 0 else str(number)+suffix


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert friendly_number(102) == '102', '102'
    assert friendly_number(10**32) == '100000000Y'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024,
                           suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(255000000000, base=1000, decimals=0, powers=[
                           '', 'k', 'M']) == '255000M'
    assert friendly_number(-155, base=100, decimals=1,
                           powers=['', 'd', 'D']) == '-1.6d'
    assert friendly_number(12000000, base=1000, decimals=3) == '12.000M'
