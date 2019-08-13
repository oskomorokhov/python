#!/usr/bin/env checkio --domain=py run largest-histogram

# https://py.checkio.org/mission/largest-histogram/

# "Your power to choose can never be taken from you.
# It can be neglected and it can be ignored.
# But if used, it can make all the difference."
# ― Steve Goodier
#
# You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.
#
# Input:List of all rectangles heights in histogram
#
# Output:Area of the biggest rectangle
#
# Example:
#
#
# largest_histogram([5]) == 5
# largest_histogram([5, 3]) == 6
# largest_histogram([1, 1, 4, 1]) == 4
# largest_histogram([1, 1, 3, 1]) == 4
# largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
# How it is used:There is no way the solution you come up with will be any useful in a real life. Just have some fun here.
#
# Precondition:
# 0 < len(data) < 1000
#
#
#
# END_DESC


def largest_histogram(histogram):

    if len(histogram) == 1:
        return histogram[0]

    if len(set(histogram)) == 1:
        return sum(histogram)

    l = []

    v_offset = 1
    count = 0

    while v_offset <= max(histogram):

        for i, b in enumerate(histogram):
            if b-v_offset >= 0:
                count += 1
            else:
                l.append((v_offset, count))
                count = 0
                continue
        else:
            l.append((v_offset, count))
            count = 0
            v_offset += 1

    return(max([x*i[n+1] for i in l for n, x in enumerate(i[:-1])]))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert largest_histogram([5]) == 5, "one is always the biggest"
    #assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    #assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    #assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    #assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    #assert largest_histogram([0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]) == False
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
    print("Done! Go check it!")
