#!/usr/bin/env checkio --domain=py run merge-intervals-iterator-version

# https://py.checkio.org/mission/merge-intervals-iterator-version/

<< << << < HEAD
# You are given a sequence of intervals, as iterator of the tuples of ints.
== == == =
# You are given a sequence of intervals, as tuples of ints where the tuples are sorted by  their first element in ascending order.
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
# It is your task to minimize the number of intervals by merging those that intersect or  by removing intervals fitting into another one. After that you have to create an iterator object which is linked to this list.
#
# Since the range of values for the intervals is restricted to integers, you must also  merge those intervals between which no value can be found.
#
# An example:
# Let's say you've got these 5 intervals:1..6, 3..5, 7..10, 9..12 and 14..16.1..6 and 3..5
<< << << < HEAD
# 3..5is a part of1..6, so3..5must disappear.1..6 and 7..10
# Even though the intervals don’t intersect, there isn’t an int type value       between them, so they have to be merged with the new interval1..10.1..10 and 9..12
# These intervals do intersect, because9 < 10,      so they have to be merged with the new interval1..12.1..12 and 14..16
# These two intervals don’t intersect, so they mustn’t be merged.So the intervals to be returned are:
# 1..12 and 14..16
#
# Input:A sequence of intervals as an iterator of the tuples of 2 ints.
== == == =
# 3..5fits into1..6, so3..5must disappear.1..6 and 7..10
# Even though the intervals do not intersect, there can not be a value of type int      between them, so they have to be merged to the new interval1..10.1..10 and 9..12
# These intervals do intersect, because9 < 10,      so they have to be merged to the new interval1..12.1..12 and 14..16
# These two intervals do not intersect, so they must not be merged.So the intervals to be returned are:
# 1..12 and 14..16
#
# Input:A sequence of intervals as a  list of tuples of 2 ints, sorted by their first element.
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
#
# Output:The iterator object linked to the list of merged intervals.
#
#
# END_DESC


def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    # Your code here
    return None


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
<< << << < HEAD
res = merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))
assert hasattr(
    res, '__iter__'), "your function should return the iterator object"
assert hasattr(
    res, '__next__'), "your function should return the iterator object"

assert list(merge_intervals(iter([(1, 4), (2, 6), (8, 10), (12, 19)]))) == [
    (1, 6), (8, 10), (12, 19)], "First"
assert list(merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))) == [
    (1, 12)], "Second"
assert list(merge_intervals(iter([(1, 5), (6, 10), (10, 15), (17, 20)]))) == [
    (1, 15), (17, 20)], "Third"
== == == =
assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [
    (1, 6), (8, 10), (12, 19)], "First"
assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [
    (1, 15), (17, 20)], "Third"
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
print('Done! Go ahead and Check IT')
