"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import time
from datetime import datetime, timedelta


def foo(*args):
    print(f"{time.ctime()}: foo was invoked")


def scheduler(foo, n):
    print(f"job {foo} is scheduled after {n}ms at {(datetime.now()+timedelta(microseconds=n*1000)).strftime('%c')}")
    time.sleep(n/1000)
    return foo(n)


if __name__ == "__main__":
    n = 5000
    scheduler(foo, n)
