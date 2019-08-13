"""
IDs
"""

twos = 0
threes = 0
with open('/Users/Krisstine/prg/python/adventofcode/2.txt', 'r') as f:
    for line in f:
        found_2 = False
        found_3 = False
        for char in line:
            if found_2 is False:
                if line.count(char) == 2:
                    twos += 1
                    found_2 = True
            if found_3 is False:
                if line.count(char) == 3:
                    threes += 1
                    found_3 = True

    print(twos*threes)
