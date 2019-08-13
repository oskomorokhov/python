#!/usr/bin/env checkio --domain=py run absolute-sorting

# https://py.checkio.org/mission/absolute-sorting/

# Let's try some sorting. Here is an array with the specific rules.
#
# The array        (a tuple)        has various numbers. You should sort it, but sort it by absolute value in ascending order.    For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).    Your function should return the sorted list  or tuple.
#
# Precondition:The numbers in the array are unique by their absolute values.
#
# Input:An array of numbers , a tuple..
#
# Output:The list or tuple (but not a generator) sorted by absolute values in ascending order.
#
# Addition:The results of your function will be shown as a list in the tests explanation panel.
#
# Precondition:    len(set(abs(x) for x in array)) == len(array)
# 0 < len(array) < 100
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
#
#
#
# END_DESC


def checkio(numbers_array):
    # how about "return sorted(numbers_array,key=abs)" ? Nah, too easy, let's do it hard way!

    t = list(numbers_array)
    srt = []
    l = []

    def check_stack(l, i):

        if l:
            if abs(i) < abs(l[:].pop()):
                #print(i,"< last item in stack",l[:].pop(),",need to swap")
                l.pop()
                l.append(i)
                #print("added&replaced",i,"in stack, stack is now",l)
                return l
            else:
                #print(i,">= last item in stack",l[:].pop(),",do nothing")
                pass
        else:
            l.append(i)
            #print("stack is empty, adding",i,"to stack, stack is now",l)

    def iter_array(t, l):

        for j, i in enumerate(t):

            if j == len(t)-1:
                #print("Last array item, check stack and terminate loop")
                check_stack(l, i)
                break

            #print("processing item",i,"in",t)
            n = t[j+1]
            #print("next item is",n)

            if abs(i) < abs(n):
                #print(i,"< next array item",n,",checking stack")
                check_stack(l, i)

            else:
                #print(i,">= next array item",n,",checking stack")
                check_stack(l, n)

        #print("l is now",l)
        srt.extend(l)
        t.remove(l.pop())
        #print("--min found & removed--")
        #print("removed from array, array is now",t)

        return srt

    while len(t) > 0:
        # print("---START---")
        #print("Array len is",len(t))
        iter_array(t, l)
        # print("---SORTED---")
        #print("srt is", srt)
        # print("---END---")

    return srt


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))
                    ) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((7, 2, 9, 3, 8, 1, 1, 2))) == [
        1, 1, 2, 2, 3, 7, 8, 9]
    assert check_it(checkio((-1, -2, -3, 0))
                    ) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
