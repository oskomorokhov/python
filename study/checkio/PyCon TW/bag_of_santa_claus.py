#!/usr/bin/env checkio --domain=py run bag-of-santa-claus

# https://py.checkio.org/mission/bag-of-santa-claus/

# When the New Year is coming, all the kids wait for a visit from Santa Claus. He comes with a huge bag of gifts, and    you can choose any one of them. But how to make the best choice? Santa takes gifts out of the bag one at a time, and    if you don't like it, he puts it back into the bag and doesn’t take it out again. This leads to some disappointing    situations when the last thing from the bag is a doll, and you already refused a pirate hat because hoping to get a    train set!
#
# When this happened with John, his Dad told him - "Don't worry,    I’ll teach you how to choose a better gift. Think about how many gifts are in the bag."
#
# Your function will be called many times in the same environment.    For each step you are given a value of the current gift,    the quantity if gifts in the current bag and a number of the current gift (counted from 1).    For each step you should make a choice to take a gift or not -- True or False.
#
# Your function will be checked repeatedly for different bags containing anywhere from 10 to 1000 gifts. We will count    only the best gifts from each bag as the second rate gifts are not for us.    All calls are running in the same environment, so be careful with globals.    You should choose 700+ the best gifts from 2000 bags.
#
# Input:Three arguments.
# current_gift- a value of the current gift as an float.
# gifts_in_bag- the quantity of gifts in a bag as an integer.
# gift_number- a number of the current gift as an integer (from 1 to gifts_in_bag).
#
#
# Output:Do you accept the current gift or not as a boolean value.
#
# Precondition:
# 10 ≤ gifts_in_bag ≤ 1000
# 0 ≤ current_gift
# Gifts are offered in the random order.
#
# END_DESC

import math


def choose_good_gift(gift_value, gifts_in_bag, gift_number):
    global best_value

    if gift_number == 1:
        best_value = 0

    if gift_value > best_value:

        if gift_number / gifts_in_bag > 1/math.e:
            return True

        best_value = gift_value

    return False


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    from random import random, randint, uniform

    scale = (random() + random()) ** randint(0, 1024)

    standings = gift_count = best_gifts = 0
    bag_count = 2000
    for i in range(bag_count):
        gifts_in_bag = randint(10, 1000)
        gift_count += gifts_in_bag

        gifts = []
        selected_gift = None
        for i in range(gifts_in_bag):
            new_gift = uniform(0., scale)
            gifts.append(new_gift)
            decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
            if decision:
                selected_gift = new_gift
                gifts.extend([uniform(0., scale)
                              for _ in range(gifts_in_bag - i - 1)])
                break
        if selected_gift is None:
            priority = len(gifts)
        else:
            priority = sum(selected_gift < x for x in gifts)
        standings += priority
        best_gifts += not priority
    print('You do won {:n} best gifts from {:n} bags with {:,} gifts!\n'
          'It seems like for bags of {:n} gifts -\n'
          'you would choose the second best gift, silver ;)'
          .format(best_gifts, bag_count, gift_count, round(gift_count / standings) + 1))
