#!/usr/bin/env checkio --domain=py run caesar-cipher-encryptor

# https://py.checkio.org/mission/caesar-cipher-encryptor/

# This mission is the part of the set. Another one -Caesar cipher decriptor.
#
# Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"
#
#
#
# Input:A secret message as a string (lowercase letters only and white spaces)
#
# Output:The same string, but encrypted
#
# Precondition:
# 0<len(text)<50
# -26<delta<26
#
#
# END_DESC


def to_encrypt(text, delta):

    import string

    alphabet = string.ascii_lowercase

    cipher = []

    for i in text.lower():
        if i == " ":
            cipher.append(" ")
            continue

        if alphabet.index(i)+delta > 26:
            cipher.append(alphabet[alphabet.index(i)-(26-delta)])
        else:
            cipher.append(alphabet[alphabet.index(i)+delta])

    return "".join(cipher)


if __name__ == '__main__':
    # print("Example:")
    #print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
