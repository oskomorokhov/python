#!/usr/bin/env checkio --domain=py run army-battles

# https://py.checkio.org/mission/army-battles/

#
# END_DESC

<< << << < HEAD
# Taken from mission The Warriors


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while all((unit_1.is_alive is True, unit_2.is_alive is True)):
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False


unit_fight = fight


class Army():
    def __init__(self):
        self.army = []

    def add_units(self, type, amount):
        self.army.extend([type() for i in range(amount)])


class Battle():
    def __init__(self):
        pass

    def fight(self, army1, army2):

        battle_is_over = False

        while battle_is_over is False:
            duel = unit_fight(army1.army[0], army2.army[0])
            if duel:
                del army2.army[0]
                if not army2.army:
                    battle_if_over = True
                    return True
            else:
                del army1.army[0]
                if not army1.army:
                    battle_if_over = True
                    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

== == == =
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
