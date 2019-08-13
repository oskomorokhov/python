"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import datetime


def count_classrooms(time_intervals: list = []) -> int:

    if not time_intervals:
        return 0

    time_intervals = sorted(time_intervals, key=lambda x: x[0])

    rooms = {}

    rooms[1] = time_intervals[0]

    for i in range(1, len(time_intervals)):
        print("checking", time_intervals[i])
        for room, interval in rooms.items():
            print("current rooms", rooms)
            if time_intervals[i][0] not in range(interval[0], interval[-1]):
                rooms[room] += time_intervals[i]
                break
        else:
            rooms[len(rooms.keys())+1] = time_intervals[i]

    print(rooms)
    return len(rooms.keys())


if __name__ == "__main__":
    time_intervals = [(30, 75), (0, 50), (60, 150)]
    assert(count_classrooms(time_intervals)) == 2
    time_intervals = [(0, 50), (60, 70), (80, 90), (100, 110), (200, 250)]
    assert(count_classrooms(time_intervals)) == 1
    time_intervals = [(0, 50), (40, 70), (60, 90), (80, 110),
                      (105, 250), (300, 320), (310, 330), (51, 59)]
    assert(count_classrooms(time_intervals)) == 2
    print("all tests complete")
