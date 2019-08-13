#!/usr/bin/env checkio --domain=py run haunted-house

# https://py.checkio.org/mission/haunted-house/

# Stephen has wandered away from the harbour and discovered a spooky old house in the woods.     After exploring it, he found that the house has 16 ( 4x4 ) rooms.    Each room has four doors, but some of those doors are blocked off, and the outer doors lead into the darkness.    The only exit from the house is the northern door in the 1st room.    While exploring the last room (#16) he heard a haunting groan followed by a grinding noise and the sound of chains rattling.    He started a sensor sweep of the house and discovered that a ghost had appeared in the first (#1) room.    Terrified, Stephen now turns to you to help him escape the house.    You'll both need to make it to the first room without encountering the ghost, for if you meet it, bad things may happen...
#
# The two of you can move in four possible directions: north, south, west and east ("N", "S", "W", "E")    as long as the doors are not blocked off. Stephen is scared and cannot stand still.    You'll need to make sure that he doesn't try to escape by any of the other outer doors as he will certainly fall into the dark abyss.    The only safe way out of the house through the northern door in first room.    On each step you should return a direction as a letter, telling Stephen where you want him to move.    After he takes a step, the ghost will make its move. The ghost knows where you and Stephen are, and is actively trying to catch you.    It cannot sit still and will always try to take the shortest path to where you and Stephen are, but it is little dumb and uses the Euclidean distance to decide which direction to move in.    If multiple directions are tied for best direction, then the ghost will randomly choose between those best directions.    You are limited to30moves, after that, the ghost summons his friends and will capture you both...
#
# On each step you are given three arguments:    the map of the house, Stephens location (room number) and the Ghosts location (room number).    The map is represented as a list with 16 elements, where each element corresponds to a room (1st element -- 1st room).    Each element on the list is a string with blocked directions.    For example: If the 6th element (index 5) is "NS", then in the 6th room the north and south doors are blocked.
# Be careful: Outer doors are always unblocked. You should exit only through the north door in the 1st room.
#
#
#
# Input:The map of the house as a list of strings,    Stephen's location (room number) and the Ghost's location (room number) as integers.
#
# Output:Stephan's move as a string.
#
# Precondition:
# 0 < stephen ≤ 16
# 0 < ghost ≤ 16
# len(house) == 16
#
#
# END_DESC


def checkio(house, stephan, ghost):
    return "N" or "S" or "W" or "E"


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    from random import choice

    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    def check_solution(func, house):
        stephan = 16
        ghost = 1
        for step in range(30):
            direction = func(house[:], stephan, ghost)
            if direction in house[stephan - 1]:
                print('Stefan ran into a closed door. It was hurt.')
                return False
            if stephan == 1 and direction == "N":
                print('Stefan has escaped.')
                return True
            stephan += DIRS[direction]
            if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
                    (stephan < 1) or (stephan > 16)):
                print('Stefan has gone out into the darkness.')
                return False
            sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
            ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
            if ghost % 4 == 1 and "W" in ghost_dirs:
                ghost_dirs.remove("W")
            if not ghost % 4 and "E" in ghost_dirs:
                ghost_dirs.remove("E")
            if ghost <= 4 and "N" in ghost_dirs:
                ghost_dirs.remove("N")
            if ghost > 12 and "S" in ghost_dirs:
                ghost_dirs.remove("S")

            ghost_dir, ghost_dist = "", 1000
            for d in ghost_dirs:
                new_ghost = ghost + DIRS[d]
                gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if ghost_dist > dist:
                    ghost_dir, ghost_dist = d, dist
                elif ghost_dist == dist:
                    ghost_dir += d
            ghost_move = choice(ghost_dir)
            ghost += DIRS[ghost_move]
            if ghost == stephan:
                print('The ghost caught Stephan.')
                return False
        print("Too many moves.")
        return False

    assert check_solution(checkio,
                          ["", "S", "S", "",
                           "E", "NW", "NS", "",
                           "E", "WS", "NS", "",
                           "", "N", "N", ""]), "1st example"
    assert check_solution(checkio,
                          ["", "", "", "",
                           "E", "ESW", "ESW", "W",
                           "E", "ENW", "ENW", "W",
                           "", "", "", ""]), "2nd example"
