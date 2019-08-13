"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, show all the ways it can be decoded.

For example, the message '111' could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

from string import ascii_lowercase as mapping
from itertools import count


def decode(source, tstr="", lst=[], cnt=count()):
    print("---foo begin---")
    print("source", source, "tstr", tstr, "lst", lst)
    if not isinstance(source, str) or not source:
        print(f"empty source, append {tstr} to {lst}")
        lst.append(tstr)
        print("lst", lst)
    elif len(source) == 1:
        print("source len is 1")
        if int(source) != 0:
            print(f"append tstr: {tstr} +  {mapping[int(source)-1]} to {lst}")
            lst.append(tstr + mapping[int(source)-1])
            print("lst", lst)
        else:
            print("source starts with 0, exit")
    else:
        print("source len > 1")
        if int(source[:1]) != 0:
            c = next(cnt)
            print(f"---recur {c} start---")
            decode(source[1:], tstr + mapping[int(source[:1])-1], lst)
            print(f"---recur {c} end---")
            if int(source[:2]) <= 26:
                print("next 2 nums in range")
                c = next(cnt)
                print(f"---recur {c} start---")
                decode(source[2:], tstr + mapping[int(source[:2])-1], lst)
                print(f"---recur {c} end---")
        else:
            print("source starts with 0, exit")
    print("returning lst", lst)
    return lst


if __name__ == "__main__":

    result = decode('10111')
    print("result", result)
