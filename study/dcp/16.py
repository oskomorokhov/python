"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class OrderLog1(object):
    # straightforward
    def __init__(self):
        self.orders = []

    def record(self, order_id):
        self.orders.append(order_id)

    def get_last(self, i):
        result = self.orders[-i]
        print(result)
        return result


class OrderLog2(object):
    # singly linked list?
    def __init__(self):
        pass

    def record(self, order_id):
        pass

    def get_last(self, i):
        pass


if __name__ == "__main__":
    log1 = OrderLog1()
    log1.record(1)
    log1.record(2)
    log1.record(3)
    log1.record(4)
    log1.record(5)
    i = 1
    assert(log1.get_last(i)) == 5
