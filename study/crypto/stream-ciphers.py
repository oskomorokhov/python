import string

literals = string.ascii_letters+string.punctuation+string.whitespace

'''
Linear Feedback shift register
'''


def stream1(i, a1=1, a2=2):
    '''
    a1,a2 (int) - taps to randomize key value
    e1,e2 (int) - initial keys (seed)
    Ei+3=a1*Ei+1+a2*Ei+2 (mod alphabet)
    '''
    e1, e2 = 2, 4
    for n in range(i):
        e3 = (a1*e1+a2*e2) % len(literals)
        yield e3
        e1, e2 = e2, e3


def encrypt1(plaintext):
    '''
    a1,a2 (int) - taps to randomize key value
    e1,e2 (int) - initial keys (seed)
    Ei+3=a1*Ei+1+2*Ei+2 (mod alphabet)
    '''
    stream = stream1(len(plaintext))
    ciphertext = ""

    for char in plaintext:
        ciphertext += literals[(literals.index(char) +
                                next(stream)) % len(literals)]

    return ciphertext


def decryp1(ciphertext):
    stream = stream1(len(ciphertext))
    plaintext = ""

    for char in ciphertext:
        plaintext += literals[(literals.index(char) -
                               next(stream)) % len(literals)]

    return plaintext


secret = encrypt1("Meet me at the fucking bar!")
print(secret)

plain = decryp1(secret)
print(plain)
