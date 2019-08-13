"""
IDs
"""


with open('/Users/Krisstine/prg/python/adventofcode/2.txt', 'r') as f:
    data = f.read().splitlines()

for i in range(0, len(data)-1):
    for j in range(1, len(data)):
        if len(set(data[i]).difference(set(data[j]))) == 1:
            print(data[i], data[j])
            break
