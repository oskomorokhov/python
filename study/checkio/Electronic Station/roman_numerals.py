#!/usr/bin/env checkio --domain=py run roman-numerals

# https://py.checkio.org/mission/roman-numerals/

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }
# END_DESC


def checkio(data):

    d_2_r = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    r_2_d = {v: k for k, v in d_2_r.items()}

    up = list(r_2_d.keys())
    down = up[::-1]

    if data in d_2_r.keys():
        return d_2_r[data]

    bases = []

    data = str(data)
    p = len(data)-1

    for d in data:
        bases.append(int(d+p*'0'))
        p -= 1
    # print(bases)

    l = []

    def rec_data(j, l):

        if j == 0:
            #print("j is 0")
            return False

        for i in down:

            if j-r_2_d[i] in (-1, -10, -100):

                #print("===time for subtruction===")
                l.append(d_2_r[abs(j-r_2_d[i])])
                l.append(i)
                break

            elif j-r_2_d[i] >= 0:

                l.append(i)
                j -= r_2_d[i]
                #print("===time for recursion===")
                if rec_data(j, l):
                    return l
                else:
                    return False

            else:
                #print("no more room, continue")
                continue

    for j in bases:
        rec_data(j, l)

    print(l)
    return ''.join(l)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'IV', '4'
    assert checkio(9) == 'IX', '9'
    assert checkio(19) == 'XIX', '19'
    #assert checkio(10) == 'X', '10'
    #assert checkio(6) == 'VI', '6'
    #assert checkio(76) == 'LXXVI', '76'
    #assert checkio(499) == 'CDXCIX', '499'
    #assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

    print("All done, press check!")
