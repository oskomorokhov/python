s = "bears like honey"
v = "aeiou"

vi = [i for i, x in enumerate(s) if x in v]

print(vi)

x = [x if x not in v else s[vi.pop()] for i, x in enumerate(s)]

print(''.join(x))
