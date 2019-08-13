from timeit import timeit


def fib_rec(num: int) -> int:
    if num <= 1:
        return num
    return fib_rec(num-1) + fib_rec(num-2)


def fib_dp(num: int, h: dict = {0: 0, 1: 1}) -> int:
    if num in h:
        return h[num]
    a = fib_dp(num-1, h)
    h[num-1] = a
    b = fib_dp(num-2, h)
    h[num-2] = b
    return a+b


def fib_iter(limit: int) -> int:
    a, b = 0, 1
    for _ in range(limit):
        a, b = b, a + b
    return a


def fib_gen(limit: int):
    a, b = 0, 1
    for _ in range(limit+1):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    num = 10
    #print("plain recursion", fib_rec(num), "within", timeit(lambda: fib_rec(num)), "s")
    #print("dynamic programming", fib_dp(num), "within", timeit(lambda: fib_dp(num)), "s")
    print("generator", [*fib_gen(num)][-1], "within",
          timeit(lambda: fib_gen(num)), "s")
    print("iterator", fib_iter(num), "within",
          timeit(lambda: fib_iter(num)), "s")
