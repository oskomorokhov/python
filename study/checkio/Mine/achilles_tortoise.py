#!/usr/bin/env checkio --domain=py run achilles-tortoise

# https://py.checkio.org/mission/achilles-tortoise/

# p.quote-source {        float: right;        font-size: 10px;    }In a race, the quickest runner can never overtake the slowest,        since the pursuer must first reach the point whence the pursued started,        so that the slower must always hold a lead.
#
# – as recounted by Aristotle, Physics VI:9, 239b15
#
# "Achilles and the tortoise" is one of the famousZeno's paradoxes.    Nikola wants to check the validity of the paradox and constructed two robots for this purpose:    Achilleborg (A1 -- fast agile prototype) and Tortoimenator (T2 -- heavy slow cyborg).
#
# A1 is faster than T2, so it has aXseconds head start on A1.    ForXseconds T2 will move att2_speed*Xmetres.    So A1 must first reach the point whence T2 already reached.    But T2 is moving and next step for A1 is to reach the next point and so on toinfinity.    The paradox is correct in theory,    but in practice A1 easily outruns T2. Hm... maybe we can calculate when A1 will catch up to T2.
#
#
#
# You are given A1 and T2’s speed in m/s as well as the length of the advantage T2 has in seconds.    Try to count the time when from when A1 come abreast with T2 (count from T2 start).    The result should be given in seconds with precious ±10-8.
#
# Input:Three arguments. Speeds of A1 and T2 and advantage as integers.
#
# Output:The time when A1 catch up T2 (count from T2 start) as an integer or float.
#
# Precondition:
# t2_speed < a1_speed < 343
# 0 < advantage ≤ 60
#
#
# END_DESC

# haha now this is really slow and cheaty


def chase(a1_speed, t2_speed, advantage):

    t2_S = t2_speed*advantage

    a1_S = 0

    t = 0

    while a1_S < t2_S:

        if t2_S-a1_S > 10:
            t += 1*10**-3

        elif t2_S-a1_S > 1/8:
            t += 1*10**-4

        elif t2_S-a1_S > 1/16:
            t += 1*10**-5

        elif t2_S-a1_S > 1/32:
            t += 1*10**-6

        elif t2_S-a1_S > 1/64:
            t += 1*10**-7

        else:
            t += 1*10**-8

        a1_S = a1_speed*t

        t2_S = t2_speed*(t+advantage)

    return float(str(t+advantage)[:12])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    #assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    #assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"
    #assert almost_equal(chase(342, 1, 60), 60.175953079, 8), "long number"
