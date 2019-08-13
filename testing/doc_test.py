def two_sum(a: int = 0, b: int = 0) -> int:
    """ Return a sum of two integers a and b
    a and b default to 0
    Test as follows
    >>> two_sum(1,2)
    3
    >>> two_sum(-1,-2)
    -3
    """
    return a+b


def square(a: int = 0):
    """ Return square of int
    a defaults to 0
    test as follows
    >>> square(1)
    1
    >>> square(2)
    4
    """
    return a**2


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("all tests completed")
