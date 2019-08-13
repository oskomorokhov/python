""" work in progress """


def _1d_array_perimeter(array: list) -> int:
    return len(array) if array else 0


def _2d_array_perimeter(array: list) -> int:
    return (_1d_array_perimeter(array) + _1d_array_perimeter(array[0]))*2 - 4


def _3d_array_perimeter(array: list) -> int:
    return _1d_array_perimeter(array) * _2d_array_perimeter(array[0]) - 3 * _1d_array_perimeter(array[0][0])


def _nd_array_perimeter(array: list) -> int:

    if not isinstance(array[0], list):
        return len(array)

    tmp = array
    x = 1

    while isinstance(tmp[0], list):
        tmp = tmp[0]
        x *= len(tmp)
    else:
        depth = len(tmp)

    y = depth * len(array)
    print(depth, x, y)
    return 2 * (x+y) - depth*4


arr1 = [0]*2
arr2 = [arr1]*3
arr3 = [arr2]*5
arr4 = [arr3]*7

arr = [[0]*10]*10

for e in arr:
    print(e)

print(_nd_array_perimeter(arr))
