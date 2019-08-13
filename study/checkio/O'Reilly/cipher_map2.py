#!/usr/bin/env checkio --domain=py run cipher-map2

# https://py.checkio.org/mission/cipher-map2/

#
# END_DESC


def recall_password(cipher_grille, ciphered_password, rotate=0, deciphered=""):

    if rotate > 3:
        return deciphered
    elif rotate == 0:
        pass
    else:
        cipher_grille = [''.join(x)[::-1] for x in zip(*cipher_grille)]

    q = [[j, i] for j, r in enumerate(cipher_grille)
         for i, w in enumerate(r) if w == 'X']

    d = [ciphered_password[i][j] for i, j in q]

    deciphered += ''.join(d)

    rotate += 1

    return recall_password(cipher_grille, ciphered_password, rotate, deciphered)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
