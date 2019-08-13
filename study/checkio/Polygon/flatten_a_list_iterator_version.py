#!/usr/bin/env checkio --domain=py run flatten-a-list-iterator-version

# https://py.checkio.org/mission/flatten-a-list-iterator-version/

#
# END_DESC


def flat_list(array):
    return array


if __name__ == '__main__':
<< << << < HEAD
res = flat_list([1, 2, 3])
assert hasattr(
    res, '__iter__'), "your function should return the iterator object"
assert hasattr(
    res, '__next__'), "your function should return the iterator object"

assert list(flat_list(iter([1, 2, 3]))) == [1, 2, 3], "First"
assert list(flat_list(iter([1, iter([2, 2, 2]), 4]))) == [
    1, 2, 2, 2, 4], "Second"
assert list(flat_list(iter([iter([2]), iter([4, iter([5, 6, iter([6]), 6, 6, 6]), 7])]))) == [
    2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
assert list(flat_list(
    iter([-1, iter([1, iter([-2]), 1]), -1]))) == [-1, 1, -2, 1, -1], "Four"
== == == =
assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [
    2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
print('Done! Check it')
