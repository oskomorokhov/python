#!/usr/bin/env checkio --domain=py run geometry-figures

# https://py.checkio.org/mission/geometry-figures/

# You often work with the different geometrical figures and with their parameters - the perimeter, area, and volume. You are tired of doing it manually, so you’ve decided to automate this process, and therefore you need to write a particular program. In this program you should create the class Parameters which will choose one of the few figures (the circle, right triangle, square, right pentagon, right hexagon, cube) using thechoose_figure()method and will count the perimeter, area, and volume with the help of the following methods:
#
# perimeter()- returns the perimeter of the figure;
# area()- returns the area of the figure;
# volume()- returns the volume of the figure.
#
# Also you have to create a class for each figure and use theStrategydesign pattern to solve this mission.
# Every figure, except the cube, has the volume = 0.
# If the result has no decimal places, you should return it as int(), in other case - round it to the 2 decimal points.
#
# Examples:
# figure = Parameters(10)
#
# figure.choose_figure(Circle())
# figure.area() == 314.16
#
# figure.choose_figure(Triangle())
# figure.perimeter() == 30
#
# figure.choose_figure(Square())
# figure.area() == 100
#
# figure.choose_figure(Pentagon())
# figure.perimeter() == 50
#
# figure.choose_figure(Hexagon())
# figure.perimeter() == 60
#
# figure.choose_figure(Cube())
# figure.volume() == 1000
#
#
#
# Input:Statements and expressions of the classes.
#
# Output:The perimeter, area, and volume (number).
#
# Precondition:All data is correct.
#
#
# END_DESC


class Parameters:
    pass


class Circle:
    pass


class Triangle:
    pass


class Square:
    pass


class Pentagon:
    pass


class Hexagon:
    pass


class Cube:
    pass


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
