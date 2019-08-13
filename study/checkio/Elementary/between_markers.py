#!/usr/bin/env checkio --domain=py run between-markers

# https://py.checkio.org/mission/between-markers/

# You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
#
# The initial and final markers are always different.If there is no initial marker then the beginning should be considered as the beginning of a string.If there is no final marker then the ending should be considered as the ending of a string.If the initial and final markers are missing then simply return the whole string.If the final marker is standing in front of the initial one then return an empty string.Input:Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
#
# Output:A string.
#
# Precondition:can't be more than one final marker and can't be more than one initial
#
#
# END_DESC


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    result = ""
    ib = text.find(begin)
    ie = text.find(end)
    ib = 0 if ib == -1 else ib+len(begin)
    ie = len(text) if ie == -1 else ie
    if (ie > ib):
        result = text[ib:ie]
    return result


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers(
        "Never send a human to do a machine's job.", "Never", "do")
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers(
        'No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
