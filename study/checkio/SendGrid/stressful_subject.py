#!/usr/bin/env checkio --domain=py run stressful-subject

# https://py.checkio.org/mission/stressful-subject/

#
# END_DESC

import string
import re


def is_stressful(subj):

    stress = False
    red = {"help", "asap", "urgent"}
    if subj[-3:] == 3*"!" or subj.isupper():
        stress = True

    subj = [i for i in subj]
    for i in subj[:]:
        if i in string.punctuation:
            subj.remove(i)
    subj = set(re.sub(r'(.)\1+', r'\1', ''.join(subj)).lower().split())
    if red.intersection(subj):
        stress = True

    return stress


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful('h-e-e-e-e-l-l-l-ppppp meeeeee') == True
    assert is_stressful("We need you A.S.A.P.!!") == True
    print('Done! Go Check it!')
