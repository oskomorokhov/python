#!/usr/bin/env checkio --domain=py run long-repeat-inside

# https://py.checkio.org/mission/long-repeat-inside/

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
#
# It is the fourth and the last mission of the series. But if in the first mission you needed to find repeating letters, then in this one you should find a repeating sequence inside the substring. I have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once, so the answer will be "ababab"
#
# Input:String.Output:String.
#
#
# END_DESC

import re


def repeat_inside(line):

    l = []

    start = 0
    end = len(line)-1
    step = 1
    recur = 1

    while start <= end:

        while step <= len(line):
            print(line[start:start+step])
            m = re.search("(?<=("+re.escape(line[start:start+step])+"){"+str(
                recur)+"})"+re.escape(line[start:start+step]), line)
            if m:
                if [m[0], recur] in l:
                    recur += 1
                    continue
                if l and l[:].pop()[0] == m[0] and l[:].pop()[1] < recur:
                    l.pop()
                    l.append([m[0], recur])
                else:
                    l.append([m[0], recur])
                recur += 1
            else:
                step += 1
                recur = 1
        else:
            start += 1
            step = 1

    l = [x for x in l if x[1] == max(list(zip(*l))[1])]
    l = sorted(l, key=lambda x: len(x[0]), reverse=True)

    return l[0][0]*(l[0][1]+1) if l else ''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert repeat_inside('aaaaa') == 'aaaaa', "First"
    #assert repeat_inside('aabbff') == 'aa', "Second"
    #assert repeat_inside('aababcc') == 'abab', "Third"
    #assert repeat_inside('abc') == '', "Forth"
    #assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
