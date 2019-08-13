def is_prime(number):
    """Return True if *number* is prime."""
    if number in (0, 1) or number < 0:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True
