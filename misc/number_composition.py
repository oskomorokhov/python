# Thanks to Dandrake @ https://dandrake.livejournal.com/83095.html


def compositions(n, k):
    if n < 0 or k < 0:
        return
    elif k == 0:
        # the empty sum, by convention, is zero, so only return something if
        # n is zero
        if n == 0:
            yield []
        return
    elif k == 1:
        yield [n]
        return
    else:
        for i in range(0, n+1):
            for comp in compositions(n-i, k-1):
                yield [i] + comp

# If you want strong compositions, in which zero isn't allowed, you can do this:


def strongcompositions(n, k):
    for c in compositions(n, k):
        if 0 not in c:
            yield c
