"""
frequency
"""

r = [0]
loop = True
while loop is True:
    with open('/Users/Krisstine/prg/python/adventofcode/1.txt', 'r') as f:
        for line in f:
            if (r[:].pop() + int(line)) in r:
                print("ans ", r[:].pop()+int(line))
                loop = False
                break
            else:
                r.append(r[:].pop()+int(line))
                print("added", r[:].pop()+int(line))
