# Pseudo-SHA

# initial string to be hashed
text = "A Test"

# convert chars in text string to their ascii values, put comma as a delimeter
text_ascii = ','.join(str(ord(c)) for c in text)

# make a list of ascii char values, comma as items separator
textarr = text_ascii.split(',')

# convert original string to binary (str) , Return an encoded version of the string as a bytes object, then Return the integer represented by the given array of bytes, then convert integer to binary
bin(int.from_bytes(text.encode(), 'big'))

# Return an iterator that applies function to every item of iterable, yielding the results.
n = map(bin, bytearray(text, 'utf8'))

# print map object
list(n)

# a way to convert string to binary (str)
bin(int.from_bytes(b"hello world", byteorder="big")).strip('0b')

# create new list, fill it with n[] items having first 2 chars ('0b') stripped and filled with zeroes till (8) for each item
m = []
for i in range(len(n)):
    m.append(n[i][2:].zfill(8))

# convert list to string, append '1'
l = ''.join(m)+'1'

# pad l with zeroes until l length is 448
while len(l) % 512 != 448:
    l += '0'

# get length of initial ascii code array, convert to bin, pad with '0's until its 64
ll = bin(len(''.join(m)))[2:].zfill(64)

# concatenate 2 stings
message = l+ll

# break message into chunks of 512, list
chunks = [message[i:i+512] for i in range(0, len(message), 512)]

# break each chunk in chunks into subarray of 32-bit words
for j in range(len(chunks)):
    q += [chunks[j][i:i+32] for i in range(0, len(chunks[j]), 32)]
