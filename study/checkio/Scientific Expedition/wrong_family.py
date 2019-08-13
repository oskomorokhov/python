#!/usr/bin/env checkio --domain=py run wrong-family

# https://py.checkio.org/mission/wrong-family/

# Michael always knew that there was something wrong with his family. Many strangers were introduced to him as part of his family.
#
# Michael should figure this out. He spent almost a month parsing family archives. He has all father-son connections of his entire family collected in one place.
#
# With all that data Michel can easily understand who the strangers are. Or maybe the only stranger in this family is Michael? Let’s see.
#
# You have a list of family relationships between father and son. Every element on this list has two elements. The first is the father's name, the second is a son’s name. All names in the family are unique. Check if the family tree is correct. There are no strangers in the family tree. All connections in the family are natural.
#
# Input:list of lists. Every element has two strings. List has at least one element
#
# Output:bool. Is family tree correct.
#
#
#
#
# Precondition:1<= len(tree)<100
#
#
# END_DESC


def is_family(tree):

    if len(tree) == 1:
        return True

    fathers = [i[0] for i in tree]

    if len(set(fathers)) == 1:
        print("one father")
        return True

    sons = [i[1] for i in tree]

    if len(set(sons)) < len(sons):
        print("father of brother")
        return False

    for i in tree[1:]:
        if i[::-1] in tree:
            print("father of father")
            return False

    print("tree", tree[::-1])
    print("fathers", fathers)
    print("sons", sons)

    for i, j in tree[::-1]:
        print(i, i in sons)
        if i not in sons:
            print("stranger")
            return False

    return True


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    '''assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'''
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    #assert is_family([["Logan","Mike"],["Alexander","Jack"],["Jack","Logan"]]) == True
    print("Looks like you know everything. It is time for 'Check'!")
