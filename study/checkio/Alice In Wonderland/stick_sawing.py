#!/usr/bin/env checkio --domain=py run stick-sawing

# https://py.checkio.org/mission/stick-sawing/

# .story img {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0,0,0,1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0,0,0,1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0,0,0,1);*/    }An enormous puppy was looking down at her with large round        eyes, and feebly stretching out one paw, trying to touch her.        "Poor little thing!" said Alice, in a coaxing tone, and she tried        hard to whistle to it; but she was terribly frightened all the        time at the thought that it might be hungry, in which case it        would be very likely to eat her up in spite of all her coaxing.
#
# Hardly knowing what she did, she picked up a little bit of        stick, and held it out to the puppy; whereupon the puppy jumped        into the air off all its feet at once, with a yelp of delight,        and rushed at the stick, and made believe to worry it; then Alice        dodged behind a great thistle, to keep herself from being run        over; and the moment she appeared on the other side, the puppy        made another rush at the stick, and tumbled head over heels in        its hurry to get hold of it; then Alice, thinking it was very        like having a game of play with a cart-horse, and expecting every        moment to be trampled under its feet, ran round the thistle        again; then the puppy began a series of short charges at the        stick, running a very little way forwards each time and a long        way back, and barking hoarsely all the while, till at last it sat        down a good way off, panting, with its tongue hanging out of its        mouth, and its great eyes half shut.
#
# "Alice's Adventures in Wonderland." Lewis Carroll
#
#
#
# A stick I found that weighed two pound:
# I sawed it up one day
# In pieces eight of equal weight!
# How much did each piece weigh?
# (Everybody says “a quarter of a pound”, which is wrong.)
#
# "Puzzles from Wonderland." Lewis Carroll
#
# The robots want to saw the stick in several pieces. The length of the stick isNinches.    We should help our robots saw the stick. All of the parts should have integer lengths (1, 2, 3 .. inches, but not    1.2).    As we love the numerical series and especially the Triangular numbers    (read more about Triangular numbers on Wikipedia),    you should saw the stick so that the lengths form the consecutive fragment of the Triangular numbers series    with the maximum quantity (fragment's length).    The parts should have different lengths (no repeating).    For example:64should divided at15, 21, 28,    because28, 36is shorter and1, 3, 15, 45is not a consecutive fragment.
#
# You are given a length of the stick (N).    You should return the list of lengths (integers) for the parts in ascending order.    If it's not possible and the problem does not have a solution, then you should return an empty list.
#
#
#
# Input:A length of the stick as an integer.
#
# Output:A fragment of the Triangular numbers as a list of integers (sorted in ascending order) or an empty list.
#
#
# END_DESC


def checkio(number):

    Tn = [x*(x+1)//2 for x in range(1, 1001)]

    for i, n in enumerate(Tn):
        c = 0
        r = 0
        while r < number:
            r = sum(Tn[i:i+c+1])
            c += 1
        else:
            if r == number:
                return Tn[i:i+c]
    else:
        return []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
