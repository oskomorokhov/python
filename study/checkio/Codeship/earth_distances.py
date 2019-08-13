#!/usr/bin/env checkio --domain=py run earth-distances

# https://py.checkio.org/mission/earth-distances/

# To describe a specific position on the surface of the Earth, we must rely on thegeographic coordinate        system.    The geographic coordinate system is a method used to give every possible location on Earth to be    specified by a set of numbers or letters. A common choice of coordinates islatitudeandlongitude.    With this information we can calculate a distance between two points along a surface.
#
# For simplicity’s sake, we will suppose that the Earth is a perfect sphere with a radius of 6,371    kilometers (it gives a mistake no more than 0.3%).    You are given two point coordinates and you must find the shortest distance between    these points on the surface of the Earth, measured along the surface of the Earth.
#
# Coordinates are given as a string with the latitude and longitude separated by comma and/or whitespace.    Latitude and longitude are represented in the follow format:
#
#
#     d°m′s″X
#
# In this example, "d" is degrees, "m" is minutes, "s" is seconds as integers, while "X" is "N"    (north) or "S" (south) for a latitude and "W" (west) or "E" (east) for a longitude.
#
# The result should be given as a number in kilometers with a precision of ±0.1 (100 metres).
#
# Input:Two arguments. Coordinates as strings (unicode).
#
# Output:The distance as a number (int or float).
#
#
#
# Precondition:Correct Coordinates.
#
#
# END_DESC

R = 6371


def distance(first, second):
    return 1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
