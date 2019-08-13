#!/usr/bin/env checkio --domain=py run bit-message

# https://py.checkio.org/mission/bit-message/

# TheBit Messageis a message that is hidden within the lines of an octet    stream and it is represented as a hexadecimal string which has maximum length    of 149 octets. The first 9 octets of the message contain theheaderfor the message and the rest comprise thecontent. The header contains 1 type octet,    7 timestamp octets, and 1 message length octet.    The content contains a maximum of 140 octets and could be    packed with either 7 bit, 8 bit or 16 bit. 7 bit packed messages    have a length of 160 characters, 8 bit packed messages have    a length of 140 characters, and 16 bit packed messages will    only have a length of 70 characters.
#
# Here are some details on the structure of a bit message:
#
#
# BIT MESSAGE FORMAT
#
#
#
#
#
#
#
#
#
#
#
# Bit76543210
#
# Octet-nth
#
#
#
#
#
#
#
#
#
# HEADER
#
#
#
#
#
#
#
# TYPE
#
#
#
#
#
#
#
#
# YEAR
#
#
#
#
#
#
#
#
# MONTH
#
#
#
#
#
#
#
#
# DAY
#
#
#
#
#
#
#
#
# HOUR
#
#
#
#
#
#
#
#
# MINUTE
#
#
#
#
#
#
#
#
# SECOND
#
#
#
#
#
#
#
#
# TIMEZONE
#
#
#
#
#
#
#
#
# LENGTH
# CONTENT
#
#
#
#
#
#
#
# Octet-1
# ...
#
#
#
#
#
#
#
# ...
#
#
#
#
#
#
#
#
#
# Octet-140
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 7-BIT PACKED MESSAGE
#
#
#
#
#
#
#
#
#
#
#
# Bit76543210
#
# Octet-nth
#
#
#
#
#
#
#
#
#
# 10b6b5b4b3b2b1b0
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 8-BIT PACKED MESSAGE
#
#
#
#
#
#
#
#
#
#
#
# Bit76543210
#
# Octet-nth
#
#
#
#
#
#
#
#
#
# 1b7b6b5b4b3b2b1b0
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 16-BIT PACKED MESSAGE
#
#
#
#
#
#
#
#
#
#
#
# Bit76543210
#
# Octet-nth
#
#
#
#
#
#
#
#
#
# 1b7b6b5b4b3b2b1b0
#
# 2b15b14b13b12b11b10b9b8
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# HEADER# OCTETDESCRIPTION
#
#
#
#
#
#
#
# TYPE1contains specific flag for specific format identifier
#
#
#
#
#
#
#
#
# DETAIL
#
#
#
#
#
# Bit 0-1 :reserved message class meaning
#
# Bit 2-3 :message encoding
#
#
# Bit 3Bit 2Pack
#
#
#
# 007 bit
#
#
#
# 018 bit
#
#
#
# 1016 bit
#
#
#
# 11reserved
#
#
#
#
#
#
#
#
# Bit 4   :reserved flag message class meaning
#
# Bit 5   :reserved message is compressed or uncompressed
# Bit 6-7 :reserved general data coding
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# TIMESTAMP7contains specificswapped nibblesfor specific format identifier
#
#
#
#
#
#
# DETAIL
#
#
#
#
#
# Octet 1YEARe.g. 10 for 2001
#
# Octet 2MONTHe.g. 10 for Jan
#
# Octet 3DAYe.g. 10 for 01
#
#
#
#
#
#
#
#
# Octet 4HOURe.g. 10 for 01
#
# Octet 5MINUTEe.g. 10 for 01
#
# Octet 6SECONDe.g. 10 for 01
#
#
#
#
#
#
#
#
# Octet 7TIMEZONEe.g. 80 for 08 x 15 / 60 = +2
#
#
# The Time Zone is GMT format, expressed in quarters of an hour. In the first of the two semi-octets, the first bit represents the algebraic sign of this difference (0 : positive, 1 : negative)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# LENGTH1maximum characters allowed is 160, 140 or 70 characters depends on message packed format
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Input data:A hexadecimal string that is a bit message (unicode).
#
# Output data:A list containing the timestamp, length of message and the message itself. The message is unicode.
#
#
# END_DESC

from datetime import datetime


def checkio(data):

    data = data.strip()

    encodings = {'00': 7, '01': 8, '10': 16, '11': 'reserved'}

    bin_stream = [bin(int(h, 16))[2:].zfill(4) for h in data[::-1]][::-1]

    bin_header_iter = iter(bin_stream[:18])
    bin_header = [c+next(iter(bin_header_iter)) for c in bin_header_iter]
    encoding = encodings[bin_header[0][::-1][2:4][::-1]]

    bin_content_iter = iter(bin_stream[18:])

    bin_content = [c+next(iter(bin_content_iter)) for c in bin_content_iter]

    length = int(bin_header[8], 2)

    bin_content_string_org = "".join(bin_stream[18::])

    if encoding == 7:
        bin_content7 = ''.join([bin_content_string_org[8*i:8*i+8][::-1]
                                for i in range(len(bin_content_string_org)//8)])
        content_string = ''.join(
            [chr(int(bin_content7[i*encoding:i*encoding+encoding][::-1], 2)) for i in range(length)])
    elif encoding == 8:
        content_string = "".join([chr(int(c, 2)) for c in bin_content])
    elif encoding == 16:
        bin_content_iter_16 = iter(bin_content)
        bin_content16 = [c+next(iter(bin_content_iter_16))
                         for c in bin_content_iter_16]
        content_string = "".join([chr(int(c, 2)) for c in bin_content16])

    bin_content_string_enc = "".join(bin_content)

    date_header = ['year', 'month', 'day',
                   'hour', 'minute', 'second', 'timezone']

    date_values = [str(int(bin_header[x][4:], 2)) +
                   str(int(bin_header[x][0:4], 2)) for x in range(1, 8)]

    timezone = str(int(bin_header[7][5:], 2))+str(int(bin_header[7][0:4], 2))

    date_values[0] = int('19'+str(date_values[0])) if int(date_values[0]
                                                          ) > 69 else int('20'+str(date_values[0]))

    date_values[6] = 'GMT +'+str(int(int(timezone)*15/60)
                                 ) if bin_header[7][4] == '0' else 'GMT -'+str(int(int(timezone)*15/60))
    if str(int(int(timezone)*15/60)) == '0':
        date_values[6] = 'GMT +0'

    date = {k: v for k, v in zip(date_header, date_values)}
    datef = datetime(int(date['year']), int(date['month']), int(
        date['day']), int(date['hour']), int(date['minute']), int(date['second']))

    return [datef.strftime("%d %b %Y %H:%M:%S")+" "+date['timezone'], length, content_string]
