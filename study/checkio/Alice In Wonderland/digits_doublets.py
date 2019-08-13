#!/usr/bin/env checkio --domain=py run digits-doublets

# https://py.checkio.org/mission/digits-doublets/

# .story .shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/    }    .story .left {        float: left;    }    .story .right {        float: right;    }    .story .title {        font-weight: bold;        margin: 20px 0 20px 0;    }
# END_DESC

paths = []


def checkio(numbers):

    global paths

    if len(numbers) < 4:
        return numbers
    else:
        find_path(numbers, numbers[0], end=numbers[-1], path=[])
        result = min(paths, key=len)
        paths = []
        return result


def find_path(numbers, start, end, path):

    if not start in path:
        path.append(start)

    if start == end:
        paths.append(path[:])
        return True

    for n in numbers:
        if n == start or n in path:
            continue
        elif [len(set(x)) for x in zip(str(start), str(n))].count(1) == 2:
            if find_path(numbers, n, end, path):
                path.pop()
    else:
        path.pop()
