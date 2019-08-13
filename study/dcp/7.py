"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.



"""

from string import ascii_lowercase as mapping


#[None for x in range(len(s)+1)]

def counter(source):
    if not source:
        return 1
    elif int(source[:2]) in range(10, 27):
        return counter(source[1:])+counter(source[2:])
    else:
        return counter(source[1:])


if __name__ == "__main__":

    cnt = counter('111')
    print("decode counter from 111 is", cnt)

    r = decode('111')
    print(r)
