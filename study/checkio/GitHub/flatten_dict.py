#!/usr/bin/env checkio --domain=py run flatten-dict

# https://py.checkio.org/mission/flatten-dict/

#
# END_DESC

<< << << < HEAD


def flatten(dictionary, d=None, temp=None):

    if d == None:
        d = {}
    if temp == None:
        temp = []

    if not any((type(x) is dict for x in dictionary.values())):

        return dictionary

    else:

        for k, v in dictionary.items():

            key = '/'.join(temp)+'/'+k if temp else k

            if not v:
                d[key] = ""

            elif type(v) == dict:
                temp.append(k)
                submerge = flatten(v, d, temp)
                if submerge == v:
                    d.update(
                        {'/'.join(temp)+'/'+i_k: i_v for i_k, i_v in v.items()})
                    temp.pop()

            else:
                d[key] = v
        else:
            if temp:
                temp.pop()

    return d


== == == =


def flatten(dictionary):
    # your code here
    return {}


>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e

if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
<< << << < HEAD

== == == =
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
assert flatten(
    {"key": {"deeper": {"more": {"enough": "value"}}}}
) == {"key/deeper/more/enough": "value"}, "Nested"
assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
<< << << < HEAD

== == == =
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
assert flatten({"name": {
    "first": "One",
    "last": "Drone"},
    "job": "scout",
    "recent": {},
    "additional": {
    "place": {
        "zone": "1",
        "cell": "2"}}}
) == {"name/first": "One",
      "name/last": "Drone",
      "job": "scout",
      "recent": "",
      "additional/place/zone": "1",
      "additional/place/cell": "2"}
<< << << < HEAD


== == == =
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
print('You all set. Click "Check" now!')
