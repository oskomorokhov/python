#!/usr/bin/env checkio --domain=py run one-line-drawing

# https://py.checkio.org/mission/one-line-drawing/

# .quote-source {        float: right;        font-size: 12px;    }“The line that describes the beautiful is elliptical.        It has simplicity and constant change. It cannot be described by a compass,        and it changes direction at every one of its points.”
#
# Rudolf Arnheim
#
# Leonardo da Vinci, Raphael, Michelangelo,        Albrecht Dürer, M.C. Escher, Hans Holbein, Paul Klee, LeRoy Neiman. All of these famous artists were left handed.
#
# Our Robots have been spending some time researching the great artists    from the Human civilization and would like to learn some of the fundamentals of art.    For their first lesson, they need to learn to control their left hand-manipulators well enough to make smooth motions.    For this exercise, they have decided to draw various figures on graph paper with an extra challenge rule --don't lift your pen.
#
# A figure is represented as a set of segments in the rectangular coordinate system.    Each segment is represented as a sequence of 4 numbers:    (x1, y1, x2, y2),    where x1, y1are coordinates for the first end and    x2, y2-- for the second.    Segments are undirected. All points in a figure are connected, so you can reach each point from any point.
#
# You should find a path in order to draw the figure.    You can pass through each segment only once and are not allowed to lift the pen.    The result must be represented as a sequence of points (tuples with coordinates)    in the order of how the pen moves to create the drawing. The path may be started and ended at any point.    If it's impossible to draw a figure then return an empty sequence. Let's look at some examples:
#
#
#
# Example 1: the figure is represented as {(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5)} and can be    two path - ((7,2),(1,2),(1,5),(4,7),(7,5)) or ((7,5),(4,7),(1,5),(1,2),(7,2)).
# Example 2: the figure {(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2)}    can not be drawn with the given rules, so the result is an empty list or tuple.
# Example 3: it's like fig.2 but with one more segment (1,5,7,5) and can be drawn several ways.    One of them ((7,2),(1,2),(1,5),(4,7),(7,5),(7,2),(1,5),(7,5),(1,2)).
#
# Input:Figure segments as a set of tuples with 4 integers each.
#
# Output:The path as a list or tuple of tuples with 2 integers each.
#
# Precondition:
# 0 < len(segments) < 30
# all(all(0 < x < 100 for x in s) for s in segments)
#
#
# END_DESC


def draw(segments):

    segments = [(x[:2], x[2:]) for x in segments]

    path = traverse_segments(segments, "cw")

    if not path:
        path = traverse_segments(segments, "ccw")
        if not path:
            return []

    return tuple([x[0] for x in path]+[path[-1][1]])


def traverse_segments(segments, direction):

    if direction == "ccw":
        segments = [x[::-1] for x in segments[::-1]]

    for i in range(0, len(segments)):
        path = []
        path.append(segments[i])

        loop = True

        while loop:

            for j in range(0, len(segments)):

                if any((segments[j] in path, segments[j][::-1] in path)):
                    continue

                elif path[-1][1] == segments[j][0]:
                    path.append(segments[j])
                    break

                elif path[-1][1] == segments[j][1]:
                    path.append(segments[j][::-1])
                    break
            else:
                loop = False

        if len(path) == len(segments):
            return path
        else:
            continue


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
                   False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
