def generate_permutations(l: list, n: int = None, prefix=None, r=[]):
    n = n if n != None else len(l)
    if prefix is None:
        prefix = []
    if n == 0:
        r.append(prefix[:])
        yield prefix[:]
        # return
    for num in l:
        if num in prefix:
            continue
        prefix.append(num)
        generate_permutations(l, n-1, prefix, r)
        prefix.pop()
    # return r


def product(*args, repeat=None):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


if __name__ == "__main__":
    A = [5, 6, 7]
    print(generate_permutations(A))
    print([*generate_permutations(A)])
    # print([*permutations(A)])
