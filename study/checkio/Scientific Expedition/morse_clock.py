#!/usr/bin/env checkio --domain=py run morse-clock

# https://py.checkio.org/mission/morse-clock/

#
# END_DESC


def checkio(time_string: str) -> str:

    l = ['0'+i if len(i) < 2 else i for i in time_string.split(':')]

    ll = [encode(binarise(l[0][0], 2)), encode(binarise(l[0][1], 4)), encode(binarise(l[1][0], 3)), encode(
        binarise(l[1][1], 4)), encode(binarise(l[2][0], 3)), encode(binarise(l[2][1], 4))]

    ll.insert(2, ':')
    ll.insert(5, ':')

    return " ".join(ll)


def binarise(digit, length):
    return bin(int(digit))[2:].zfill(length)


def encode(input):
    return "".join(['.' if i == '0' else '-' for i in input])


if __name__ == '__main__':
    # print("Example:")
    # print(checkio("10:37:49"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(
        "21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(
        "23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
