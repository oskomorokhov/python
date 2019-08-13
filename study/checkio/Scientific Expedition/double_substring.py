#!/usr/bin/env checkio --domain=py run double-substring

# https://py.checkio.org/mission/double-substring/

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
#
# This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length. You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps. For example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")
#
# Input:String.Output:Int.
#
#
#
#
# END_DESC


def double_substring(line):

    # define how far we can look ahead
    max = len(line)//2

    # we'll place our matches here
    match = []

    # enumerate the line to have indexes of each char and loop though it
    for i, c in enumerate(line):

        # inner loop will calc length of steps we take from current char's index
        for step in range(1, max+1):

            # if we are here, our step length has gone beyond length of line so we need to abort
            if i+step >= len(line):
                break

            # if str between current char's index and (current char's index + current step) was found in the remaining portion of line (AFTER current char's index + current step) - we have a match
            if line[i:i+step] in line[i+step:]:
                match.append(line[i:i+step])

    # sort the list by length of elements, starting with max, and return length of 1st element. Return 0 is the list is empty.
    return len(sorted(match, key=len, reverse=True)[0]) if match else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
