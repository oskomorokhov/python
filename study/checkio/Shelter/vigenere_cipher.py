#!/usr/bin/env checkio --domain=py run vigenere-cipher

# https://py.checkio.org/mission/vigenere-cipher/

# TheVigenère cipheris a method of encrypting alphabetic text by using a series of different Caesar ciphers based on    the letters of a keyword. It is a simple form of polyalphabetic substitution.
#
# In the Vigenère cipher each letter of a message is shifted along some number of places with different shift values.    To encrypt, a table of alphabets can be used, termed a tabula recta, Vigenère square, or Vigenère table. It consists    of the alphabet written out 26 times in different rows, each version of the alphabet is shifted    cyclically to the left compared to the    previous alphabet.    At different points in the encryption process, the cipher uses a different alphabet from one of the rows.    The alphabet used at each point depends on a repeating keyword.
#
#
# \  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#  \----------------------------------------------------
# A| A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# B| B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# C| C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
# D| D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
# E| E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
# F| F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
# G| G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
# H| H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
# I| I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
# J| J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
# K| K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
# L| L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
# M| M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
# N| N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
# O| O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
# P| P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
# Q| Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
# R| R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
# S| S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
# T| T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
# U| U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
# V| V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
# W| W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
# X| X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
# Y| Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
# Z| Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
#
# To see how this works, lets take, the message "DONTWORRYBEHAPPY" and the keyword "CHECKIO". Write the message and    the keyword below,    then shift each letter in the message related by corresponded letter in the repeating keyword.
#
#
# Message:   DONTWORRYBEHAPPY
# Key:       CHECKIOCHECKIOCH
# Encrypted: FVRVGWFTFFGRIDRF
#
# Vigenère can also be viewed algebraically. If the letters A–Z are taken to be the numbers 0–25, and addition is    performed modulo 26, then Vigenère encryption E using the key K can be written as:
# Ci= Ek(Mi) = (Mi+ Ki) % 26
#
# Now, consider the following scenario: you and your friend use that cipher for correspondence and you've forgot the    key. But, to your luck, you have an archive with encrypted and decrypted message. With that you can find the key and    decrypt the new fresh message from your friend.
#
# Input:Three arguments. An old decrypted message, an old encrypted message and a new encrypted    message as strings (unicode for py2).
#
# Output:The new decrypted message as a string.
#
# Precondition:
# all(re.match("[A-Z]+\Z", text) for text in args)
# len(key) ≤ len(old_encrypted)
# 2 * len(key)<= len(old_encrypted)<len(new_encrypted) or len(new_encrypted)<= len(old_encrypted)
#
#
# END_DESC

import string


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    '''
    Ci=(Mi+Ki)%26 
    Ki%26=Ci-Mi%26
    Mi%26=Ci-Ki%26
    '''
    key = []
    new_decrypted = ""

    for i, c in enumerate(old_encrypted):
        Ci = string.ascii_uppercase.index(c)
        Mi = string.ascii_uppercase.index(old_decrypted[i])
        Ki = (Ci-Mi) % 26
        key.append(Ki)

    if len(new_encrypted) > len(key):
        for c in key:
            if key.count(c) % 2 != 0:
                key = key[:-1]

    for i, c in enumerate(new_encrypted):
        Ki = key[i % len(key)]
        new_decrypted += string.ascii_uppercase[(
            string.ascii_uppercase.index(c)-Ki)]

    return new_decrypted


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere(u"AAAAAAAAA", u"ABABABABC",
                           u"ABABABABC") == "AAAAAAAAA"
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
    assert decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT", u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI",
                           u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL") == "IMALUMBERJACKANDIMOKISLEEPALLNIGHTANDIWORKALLDAYICUTDOWNTREESISKIPANDJUMPILIKETOPRESSWILDFLOWERSIPUTONWOMENSCLOTHINGANDHANGAROUNDINBARS"
