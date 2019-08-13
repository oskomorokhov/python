#!/usr/bin/env checkio --domain=py run multiplication-table

# https://py.checkio.org/mission/multiplication-table/

# .story .shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/    }    .t-example {        text-align: center;        margin: 0 auto 0 auto;    }    .t-example tr:first-child td{        border-bottom: solid #294270 2px;    }    .t-example tr:last-child td {        border-top: solid #294270 2px;    }        .t-example td .operation {        border-collapse: collapse;        margin: 5px;    }    .t-example td {        color: #294270;    }        .t-example td .operation td {        border: solid #294270 1px;        font-size: 14px;        font-weight: bold;        padding: 2px;        color: #294270;    }    .t-example td .operation tr:first-child td {        border: none;    }    .t-example td .operation tr:last-child td,    .t-example td .operation tr td.td-sum    {        border-bottom: none;    }    .t-example td .operation tr td:first-child {        border-left: none;    }    .t-example td .operation tr td:last-child {        border-right: none;    }    .td-header {        font-size: 20px;    }    .td-result {        font-size: 16px;    }Alice took up the fan and gloves, and, as the hall was very        hot, she kept fanning herself all the time she went on talking:        'Dear, dear! How queer everything is to-day! And yesterday        things went on just as usual. I wonder if I've been changed in        the night? Let me think: was I the same when I got up this        morning? I almost think I can remember feeling a little        different. But if I'm not the same, the next question is, Who in        the world am I? Ah, THAT'S the great puzzle!' And she began        thinking over all the children she knew that were of the same age        as herself, to see if she could have been changed for any of        them.
#
# "I'm sure I'm not Ada," she said, "for her hair goes in such        long ringlets, and mine doesn't go in ringlets at all; and I'm        sure I can't be Mabel, for I know all sorts of things, and she,        oh! she knows such a very little! Besides, SHE'S she, and I'm I,        and--oh dear, how puzzling it all is! I'll try if I know all the        things I used to know. Let me see: four times five is twelve,        and four times six is thirteen, and four times seven is--oh dear!        I shall never get to twenty at that rate! However, the        Multiplication Table doesn't signify:...
#
# "Alice's Adventures in Wonderland." Lewis Carroll
#
#
#
# After reading "Alice's Adventures in Wonderland,"    our robots decided to create their own "Multiplication table."    Stephan would lead this mission (yeah, that probably was a bad idea).    He forgot how to do multiplication and tried to invent a new method.    It’s a rather strange method if we may be so blunt.
#
# In Stephan's version of multiplication, we convert numbers to binary representation without leading zeroes.    Then the first number is written vertically (up to down) and the second horizontally (left to right).    With that, we fill a table with various binary operations for each crossing -- AND, OR, XOR, so we end up with three tables.    In each table we convert rows to decimal and summarize it,    then summarize the results of three tables. Let's look at several examples.
#
# 4 x 6 =ANDX110decsum1110660000000000ORX110decsum11117190110601106XORX110sum100111301106011066 + 19 + 13 =38
#
# 2 x 7 =ANDX111decsum11117700000ORX111decsum111171401117XORX111sum100007011177 + 14 + 7 =28
#
# 7 x 2 =ANDX10decsum1102611021102ORX10decsum1113911131113XORX10sum10113101110116 + 9 + 3 =18You should help Stephan write a function to calculate this "multiplication".    You are given two positive integers (n > 0), be careful with order of arguments.
#
# Input:Two arguments as integers.
#
# Output:The result of the Stephan's "multiplication", an integer.
#
# Precondition:0<x<100
# 0<y<100
#
#
#
# END_DESC


def checkio(first, second):

    x = bin(first)[2:]
    y = bin(second)[2:]

    la = [[] for _ in x]
    lo = [[] for _ in x]
    lx = [[] for _ in x]

    for j, c in enumerate(x):
        for r in y:
            la[j].append(str(int(c) & int(r)))
            lo[j].append(str(int(c) | int(r)))
            lx[j].append(str(int(c) ^ int(r)))

    return sum([int(''.join(a), 2) for a in la+lo+lx])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
