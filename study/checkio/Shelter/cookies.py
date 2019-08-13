#!/usr/bin/env checkio --domain=py run cookies

# https://py.checkio.org/mission/cookies/

# This is pretty much a technical mission.
#
# You have rawHTTP cookies. Your mission is to extract the value of a specific cookie by its name.
#
# Input:Two arguments. Both are strings. The first one is the string of raw cookies, and the second one is the name of the cookie we are looking for.
#
# Output:A string. Extracted value.
#
#
#
# END_DESC

import re


def get_cookie(cookie, name):

    cookie = {x[0]: x[1]
              for x in [x.split('=', maxsplit=1) for x in cookie.split('; ')]}

    return cookie[name]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123',
                      'theme') == 'light', 'theme=light'
    assert get_cookie(
        '_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    assert get_cookie("USER=name=Unknown; domain=bbc.com",
                      "USER") == "name=Unknown"
    print("Looks like you know everything. It is time for 'Check'!")
