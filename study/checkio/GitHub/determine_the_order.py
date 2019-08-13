#!/usr/bin/env checkio --domain=py run determine-the-order

# https://py.checkio.org/mission/determine-the-order/

# The Robots have found an encrypted message. We cannot decrypt it at the moment,    but we can take the first steps towards doing so. You have a set of "words", all in lower case, and each word contains    symbols in "alphabetical order". (it's not your typical alphabetical order, but a new and different order.)    We need to determine the order of the symbols from each "word" and create a single "word" with all of these symbols,    placing them in the new alphabetial order.    In some cases, if we cannot determine the order for several symbols, you should use the traditionallatin alphabetical        order.    For example:    Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a"    and "d" after "b". So the result is "zwacbd".Input:Words as a list of strings.
#
# Output:The order as a string.
#
# Precondition:For each test, there can be the only one solution.
# 0<|words|<10
#
#
# END_DESC

import string
<< << << < HEAD


def checkio(data):

    seq = []
    temp = []
    marker = []

    for word in data:
        print("-----")
        print(f"begin word {word}")
        for symbol in word:
            print(f"{symbol} in {word}")
            if symbol in temp:
                print('duplicate, skip')
                continue
            else:
                temp.append(symbol)
                print(f"{symbol} appended, temp is {temp}")
        else:
            print(f"end word {word}")
            print("-----")
            print(f"begin temp {temp}")
            pos = None
            for symbol in temp[:]:
                if symbol in seq:
                    offset = 1
                    pos = seq.index(symbol)
                    print(f"{symbol} in seq, pos {pos}")
                    temp.remove(symbol)
                    print(f"{symbol} removed from temp")
                    print("pos", pos)
                    continue
                else:
                    if pos is None:
                        print(f"{symbol} not in seq and pos is None, continue")
                        continue
                    else:
                        seq.insert(pos+offset, symbol)
                        print(f"inserted {symbol} into seq after {seq[pos]}")
                        print(f"seq {seq}")
                        offset += 1
                        print(f"offset {offset}")
                        temp.remove(symbol)
                        print(f"{symbol} removed from temp")

            else:
                print("-----")
                print(f"end temp")
                if temp:
                    print(f"temp is {temp}")
                    if pos is None:
                        print("no pos")
                        seq.extend(temp)
                    else:
                        print("last item was in seq, we have pos")
                        seq[pos:pos] = temp

            print(f"seq {seq}")
            del temp[:]
            print("temp erased")

    print(f"final seq {seq}")
    return ''.join(seq)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    assert checkio(["my", "name", "myke"]) == "namyke"

    assert checkio(["hello", "low", "lino", "itttnosw"]) == "helitnosw"

== == == =


def checkio(data):
    return ""


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
    "Just concatenate it"
assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
    "Paste in"
assert checkio(["a", "b", "c"]) == "abc", \
    "Cant determine the order - use english alphabet"
assert checkio(["aazzss"]) == "azs", \
    "Each symbol only once"
assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
    "Concatenate and paste in"
