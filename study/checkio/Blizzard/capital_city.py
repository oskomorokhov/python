#!/usr/bin/env checkio --domain=py run capital-city

# https://py.checkio.org/mission/capital-city/

# You are an active traveler who have visited a lot of countries. The main city in the every country is its capital and each country can have only one capital city.So your task is to create the class Capital which has some special properties: the first created instance of this class will be unique and single, and all of the other instances should be the same as the very first one.
# Also you should add thename()method which returns the name of the capital.
# In this mission you should use theSingletondesign pattern.
#
# Example:
# ukraine_capital_1 = Capital("Kyiv")
# ukraine_capital_2 = Capital("London")
# ukraine_capital_3 = Capital("Marocco")
# ukraine_capital_2.name() == "Kyiv"
# ukraine_capital_3.name() == "Kyiv"
#
#
#
# Input:The class Capital.
#
# Output:The name of the capital.
#
# Precondition:All data is correct.
#
#
# END_DESC

# https://www.python.org/download/releases/2.2.3/descrintro/#__new__


class Singleton(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass


class Capital(Singleton):

    def init(self, city_name=None):
        self.city_name = city_name

    def name(self):
        return self.city_name


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
